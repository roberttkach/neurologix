from fastapi import FastAPI
from uvicorn import run
from API.model_zip import app as zip_app

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.mount("/model", zip_app)

if __name__ == "__main__":
    run(app)
