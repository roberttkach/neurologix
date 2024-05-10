import http.client
import json
import time
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

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


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        conn = http.client.HTTPConnection('192.168.31.1')
        headers = {'Content-type': 'application/json'}
        conn.request('POST', '/receive_data', json.dumps(data), headers)
        response = conn.getresponse()
        print(response.read().decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data sent")


def handler(*args, **kwargs):
    return RequestHandler(*args, **kwargs)


def run(server_class=HTTPServer, handler_class=handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
