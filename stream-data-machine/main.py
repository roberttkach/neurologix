import time
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from fastapi import FastAPI
import requests
import json

app = FastAPI()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'stream_data', default_args=default_args, schedule_interval=timedelta(1)
)


def process_data():
    data = pd.read_csv('data/tmnist.csv')
    y = data['labels'].values
    X = data.drop(['names', 'labels'], axis=1).values
    counter = 0
    while counter <= data.shape[0]:
        X, y = X[counter], y[counter]
        time.sleep(0.2)
        counter += 1
    return X, y


process_data = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)


@app.post("/send_data")
async def send_data(data: dict):
    response = requests.post('http://192.168.31.1/receive_data', data=json.dumps(data))
    return {"message": "Data sent", "response": response.text}
