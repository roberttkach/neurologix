from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
import shutil
import os
import zipfile

app = FastAPI()


@app.post("/uploadzip/")
async def upload_zip(file: UploadFile = File(...)):
    if file.filename.endswith(".zip"):
        file_location = os.path.join("containers", file.filename)
        with open(file_location, 'wb+') as f:
            shutil.copyfileobj(file.file, f)

        with zipfile.ZipFile(file_location, 'r') as zip_ref:
            zip_ref.extractall("containers")

        return JSONResponse(status_code=200, content={"message": "File uploaded and unzipped successfully"})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip file.")
