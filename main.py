from fastapi import FastAPI
from uvicorn import run
from API.model_zip import app as zip_app
from API.model_sevenz import app as sevenz_app

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать на мой веб-сайт!",
        "instructions": "Используйте /model для доступа к модели.",
        "author": "Ваше имя"
    }


app.mount("/model", zip_app)
app.mount("/model", sevenz_app)

if __name__ == "__main__":
    run(app)
