import logging
import os
from fastapi import FastAPI
from uvicorn import Config, Server
from API.archive import router as archive_router
import asyncio

app = FastAPI()

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='logs.log', level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    logger.info("Root endpoint hit.")
    return {
        "message": "Welcome to NeuroLogix!",
        "instructions": "Use /archive to upload your model into a new container.",
        "author": "Group Delta"
    }


app.include_router(archive_router)


async def main():
    global port
    try:
        port = int(os.getenv('PORT', 8000))
        config = Config(app=app, host="0.0.0.0", port=port)
        server = Server(config)
        logger.info(f"FastAPI server started on port {config.port}.")
        await server.serve()
    except Exception as e:
        logger.error(f"Error starting FastAPI server on port {port}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
