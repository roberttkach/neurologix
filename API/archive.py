from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import zipfile


app = FastAPI()


@app.post("/uploadzip/")
async def upload_zip(file: UploadFile = File(...)):
    if file.filename.endswith(".zip"):
        some_condition = Path("containers").exists()
        if some_condition:
            file_location = Path("containers") / file.filename
        else:
            file_location = Path("/containers") / file.filename

        with open(file_location, 'wb+') as f:
            shutil.copyfileobj(file.file, f)

        with zipfile.ZipFile(file_location, 'r') as zip_ref:
            zip_ref.extractall(Path("containers") / "your_project_directory")

        return JSONResponse(status_code=200, content={"message": "File uploaded and unzipped successfully"})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip file.")
