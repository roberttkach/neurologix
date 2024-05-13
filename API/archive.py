from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import zipfile

router = APIRouter()


@router.post("/archive/")
async def upload_zip(file: UploadFile = File(...), name: str = Form(...)):
    if file.filename.endswith(".zip"):
        file_location = Path("containers") / file.filename

        file_location.parent.mkdir(parents=True, exist_ok=True)

        with open(file_location, 'wb+') as f:
            shutil.copyfileobj(file.file, f)

        with zipfile.ZipFile(file_location, 'r') as zip_ref:
            extract_location = Path("containers") / name
            extract_location.mkdir(parents=True, exist_ok=True)
            zip_ref.extractall(extract_location)

        return JSONResponse(status_code=200, content={"message": f"File {name} uploaded and unzipped successfully"})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip file.")
