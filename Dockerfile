FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 9090

CMD ["python3", "main.py"]
