import os
import asyncio

from prometheus_client import start_http_server, Counter
from concurrent.futures import ThreadPoolExecutor

uploaded_files_total = Counter('uploaded_files_total', 'Total uploaded files')


def update_counter():
    folders = [name for name in os.listdir('containers') if os.path.isdir(os.path.join('containers', name))]
    uploaded_files_total.inc(len(folders))


async def async_update_counter():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, update_counter)


start_http_server(8080)
asyncio.run(async_update_counter())
