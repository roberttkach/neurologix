from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from classification import process_image
from classification import process_image

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Чтение изображения из файла
    image = await file.read()

    # Отправка изображения на сервер Go
    response = requests.post('http://localhost:8080/upload', files={'file': image})

    return {"image_id": response.json()['image_id']}

@app.post("/process")
async def process_image_endpoint(file: UploadFile = File(...)):
    image_stream = io.BytesIO(await file.read())
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)

    processed_image = process_image(file_bytes)

    return {"image": processed_image}
