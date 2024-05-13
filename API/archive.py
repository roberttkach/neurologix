from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import zipfile
import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import zipfile



'''
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

from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import zipfile
import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import zipfile


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



from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import zipfile
import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import zipfile



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

from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import zipfile
import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import zipfile




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
'''


import logging
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import zipfile

logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/archive/")
async def upload_zip(file: UploadFile = File(...), name: str = Form(...)):
    logging.info(f"Received file {file.filename}")
    if file.filename.endswith(".zip"):
        ml_dirs = sorted([d for d in Path(r"\neurologix\containers").iterdir() if d.is_dir() and d.name.startswith("ML")])
        new_dir = "ML1" if not ml_dirs else f"ML{int(ml_dirs[-1].name[2:]) + 1}"
        file_location = Path(r"\neurologix\containers") / file.filename
        extract_location = Path(r"\neurologix\containers") / new_dir


        file_location.parent.mkdir(parents=True, exist_ok=True)
        extract_location.mkdir(parents=True, exist_ok=True)

        with open(file_location, 'wb+') as f:
            shutil.copyfileobj(file.file, f)

        with zipfile.ZipFile(file_location, 'r') as zip_ref:
            if "requirements.txt" not in zip_ref.namelist() or "train.py" not in zip_ref.namelist():
                raise HTTPException(status_code=400, detail="Zip file must contain requirements.txt and train.py")
            zip_ref.extractall(extract_location)

        with open(extract_location / "Dockerfile", 'w') as f:
            f.write("FROM python:3.8-slim\n")
            f.write("COPY . /app\n")
            f.write("WORKDIR /app\n")
            f.write("RUN pip install -r requirements.txt\n")
            f.write("CMD [\"python\", \"train.py\"]\n")

        os.system(f"docker build -t {new_dir.lower()} {extract_location}")

        return JSONResponse(status_code=200, content={"message": f"File {name} uploaded, unzipped, and Docker image built successfully"})
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a zip file.")
        


