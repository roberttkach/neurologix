FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Запустите main.py
CMD ["python3", "k8s_script.py", "main.py"]
