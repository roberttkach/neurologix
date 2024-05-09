# Используйте официальный образ Python 3.12.3
FROM python:3.12.3

# Установите рабочую директорию в /app
WORKDIR /app

# Скопируйте текущий каталог в рабочую директорию
COPY . /app

# Установите необходимые пакеты
RUN pip install -r requirements.txt \
    --timeout=120 \
    --retries=10 \
    --trusted-host=pypi.org \
    --trusted-host=pypi.python.org \
    --trusted-host=files.pythonhosted.org \
    --trusted-host=pypi.doubanio.com \
    --trusted-host=pypi.tuna.tsinghua.edu.cn \
    --index-url=https://pypi.org/simple \
    --extra-index-url=https://pypi.doubanio.com/simple \
    --extra-index-url=https://pypi.tuna.tsinghua.edu.cn/simple

# Откройте порт 8000 для FastAPI
EXPOSE 8000

# Запустите приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
