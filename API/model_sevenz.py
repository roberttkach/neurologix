from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
import shutil
import os
import py7zr

app = FastAPI()

@app.post("/upload7z/")
async def upload_7z(file: UploadFile = File(...)):
    if file.filename.endswith(".7z"):
        file_location = os.path.join("containers", file.filename)
        with open(file_location, 'wb+') as f:
            shutil.copyfileobj(file.file, f)

        with py7zr.SevenZipFile(file_location, mode='r') as z:
            z.extractall("containers")

        return JSONResponse(status_code=200, content={"message": "File uploaded and unzipped successfully"})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a 7z file.")
