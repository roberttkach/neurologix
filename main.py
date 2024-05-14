import logging
import os

from fastapi import FastAPI
from uvicorn import Config, Server
from API.archive import router as archive_router
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='logs.log', level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to NeuroLogix!",
        "instructions": "Use /archive to upload your model into a new container.",
        "author": "Group Delta"
    }


app.include_router(archive_router)


async def run_app():
    config = Config(app=app, host="localhost", port=8080)
    server = Server(config)
    logger.info(f"FastAPI server started on port {config.port}.")
    await server.serve()


def run_prometheus():
    logger.info("Prometheus started.")
    os.system("python metrics/prometheus.py")


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, run_prometheus)
    await run_app()


if __name__ == "__main__":
    asyncio.run(main())
