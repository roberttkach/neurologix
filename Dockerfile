FROM ubuntu:24.04

RUN apt-get update && apt-get install -y python3.12.3 python3-pip
RUN apt-get update && apt-get install -y golang-1.22.2
RUN apt-get update && apt-get install -y mongodb

COPY requirements.txt ./
COPY go.mod ./

RUN pip3 install -r requirements.txt

RUN go mod download

COPY . .

CMD ["python3", "main.py"]
