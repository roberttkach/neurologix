import logging
import shutil
import subprocess
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import zipfile
import py7zr
import rarfile
import tarfile

router = APIRouter()


def create_dockerfile(path: Path):
    with open(path / "Dockerfile", 'w') as f:
        f.write("FROM python:3.8-slim\n")
        f.write("COPY . /app\n")
        f.write("WORKDIR /app\n")
        f.write("RUN pip install -r requirements.txt\n")
        f.write("CMD [\"python\", \"train.py\"]\n")


@router.post("/archive")
async def upload(file: UploadFile = File(...), name: str = Form(...)):
    logging.info(f"Received file {file.filename}")
    if file.filename.endswith((".zip", ".7z", ".rar", ".tar.gz")):
        dir_path = Path("neurologix/containers") / name
        if dir_path.exists():
            raise HTTPException(status_code=400, detail="Container with this name already exists.")
        else:
            file_location = Path("neurologix/cache") / file.filename
            extract_location = dir_path

            file_location.parent.mkdir(parents=True, exist_ok=True)
            extract_location.mkdir(parents=True, exist_ok=True)

            with open(file_location, 'wb+') as f:
                shutil.copyfileobj(file.file, f)

            try:
                file_types = {
                    ".zip": zipfile.ZipFile,
                    ".7z": py7zr.SevenZipFile,
                    ".rar": rarfile.RarFile,
                    ".tar.gz": tarfile.open
                }

                for ext, archive in file_types.items():
                    if file.filename.endswith(ext):
                        with archive(file_location, 'r') as arch:
                            if ext == ".tar.gz":
                                namelist = arch.getnames()
                            else:
                                namelist = arch.namelist()

                            if "requirements.txt" not in namelist or "train.py" not in namelist:
                                raise HTTPException(status_code=400,
                                                    detail=f"{ext} file must contain requirements.txt and train.py.")
                            arch.extractall(path=extract_location)
                        break
                else:
                    raise HTTPException(status_code=400, detail="File type not supported.")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

            create_dockerfile(extract_location)

            build_result = subprocess.run(f"docker build -t {name.lower()} {extract_location}", shell=True, check=False)
            if build_result.returncode != 0:
                raise HTTPException(status_code=500, detail="Docker build failed.")

            return JSONResponse(status_code=200,
                                content={
                                    "message": f"File {name} uploaded, unzipped, and Docker image built successfully."})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip, 7z, rar, or tar.gz file.")
