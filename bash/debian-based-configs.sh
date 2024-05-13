#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev apt-utils systemd
wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
tar -xvf Python-3.12.3.tgz || exit
cd Python-3.12.3 || exit
./configure --enable-optimizations
sudo make altinstall
sudo apt-get install -y python3-pip
pip3 install -r requirements.txt
sudo apt-get install gnupg curl -y && \
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-7.0.gpg && \
echo "deb [signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg] http://repo.mongodb.org/apt/debian buster/mongodb-org/7.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list && \
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list && \
sudo apt-get update && \
sudo apt-get install libssl1.1 && \
sudo apt-get install -y mongodb-org && \
sudo systemctl start mongod && \
sudo systemctl enable mongod && \
sudo rm /etc/apt/sources.list.d/focal-security.list

echo "export PATH=/usr/local/bin:${PATH}" >> ~/.bashrc
source ~/.bashrc
