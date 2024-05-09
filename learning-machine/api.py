from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    data: dict

@app.post("/receive_data")
async def receive_data(item: Item):
    return {"message": "Data received", "data": item.data}
