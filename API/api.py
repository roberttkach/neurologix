from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()


@app.post("/uploadzip/")
async def upload_zip(file: UploadFile = File(...)):
    if file.filename.endswith(".zip"):
        with open(os.path.join("your_directory", file.filename), 'wb+') as f:
            shutil.copyfileobj(file.file, f)
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip file.")
