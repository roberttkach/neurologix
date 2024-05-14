import asyncio
import logging
import os
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
        dir_path = Path("containers") / name
        file_location = Path("cache") / file.filename
        extract_location = dir_path

        if dir_path.exists():
            raise HTTPException(status_code=400, detail="Container with this name already exists.")

        file_location.parent.mkdir(parents=True, exist_ok=True)
        extract_location.mkdir(parents=True, exist_ok=True)

        try:
            with open(file_location, 'wb+') as f:
                shutil.copyfileobj(file.file, f)

            file_types = {
                ".zip": zipfile.ZipFile,
                ".7z": py7zr.SevenZipFile,
                ".rar": rarfile.RarFile,
                ".tar.gz": tarfile.open
            }

            for ext, archive in file_types.items():
                if file.filename.endswith(ext):
                    with archive(file_location, 'r') as arch:
                        arch.extractall(path=extract_location)
                        data_location = Path(extract_location) / file.filename
                        data_location = data_location.with_suffix('')

                        if os.path.exists(data_location):
                            files = os.listdir(data_location)
                            for file in files:
                                old_path = os.path.join(data_location, file)
                                new_path = os.path.join(extract_location, file)
                                shutil.move(old_path, new_path)
                                print(f"{old_path} >> {new_path}")

                            shutil.rmtree(data_location)

                        required_files = ["requirements.txt", "train.py"]
                        if not all(os.path.exists(os.path.join(extract_location, file)) for file in required_files):
                            dir_content = os.listdir(extract_location)
                            dir_content_str = ', '.join(dir_content)
                            raise HTTPException(status_code=400,
                                                detail=f"{ext} file must contain requirements.txt and train.py. Current directory content: {dir_content_str}")
                    break
            else:
                raise HTTPException(status_code=400, detail="File type not supported.")

            create_dockerfile(extract_location)

            build_result = subprocess.run(f"docker build -t {name.lower()} {extract_location}", shell=True, check=False)
            if build_result.returncode != 0:
                raise HTTPException(status_code=500, detail="Docker build failed.")

            return JSONResponse(status_code=200,
                                content={
                                    "message": f"File {name} uploaded, unzipped, and Docker image built successfully."})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            try:
                if file_location.exists():
                    file_location.unlink()
            except Exception as cleanup_error:
                logging.error(f"Error during cleanup: {cleanup_error}")
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip, 7z, rar, or tar.gz file.")

