# Используйте образ Ubuntu 24.04
FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install -r requirments.txt

# Запустите main.py
CMD ["python3", "k8s_script.py", "script.py"]
