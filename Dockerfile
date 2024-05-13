# Используйте образ Ubuntu 24.04
FROM ubuntu:24.04

# Обновите систему и установите необходимые пакеты
RUN apt-get update -y && apt-get install -y sudo wget

# Копируйте файл debian-based-configs.sh из папки bash в контейнер
COPY bash/debian-based-configs.sh .

# Дайте разрешение на выполнение файла
RUN chmod +x debian-based-configs.sh

# Запустите файл debian-based-configs.sh
RUN ./debian-based-configs.sh

# Копируйте main.py в контейнер
COPY main.py .

# Запустите main.py
CMD ["python3", "main.py"]
