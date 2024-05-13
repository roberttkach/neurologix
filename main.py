from fastapi import FastAPI
from uvicorn import run
from API.archive import router as archive_router

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в NeuroLogix!",
        "instructions": "Используйте /archive для загрузки своей модели в новый контейнер.",
        "author": "Ваше имя"
    }


app.include_router(archive_router, prefix="/archive")

if __name__ == "__main__":
    run(app)
