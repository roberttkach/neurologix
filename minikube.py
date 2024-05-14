import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

containers_dir = "containers"


def generate_k8s_manifest(container_name):
    return f"""
apiVersion: v1
kind: Pod
metadata:
  name: {container_name}-pod
spec:
  containers:
  - name: {container_name}
    image: {container_name}:latest
"""


if not os.path.exists(containers_dir):
    raise FileNotFoundError(f'Ошибка: Директория {containers_dir} не существует.')
else:
    containers = os.listdir(containers_dir)
    if not containers:
        raise ValueError(f'Ошибка: Директория {containers_dir} пуста.')
    else:
        for container in containers:
            container_path = os.path.join(containers_dir, container)

            if os.path.isdir(container_path):
                dockerfile_path = os.path.join(container_path, 'Dockerfile')

                if os.path.exists(dockerfile_path):
                    subprocess.run(['docker', 'build', '-t', f'{container}:latest', container_path])

                    k8s_manifest = generate_k8s_manifest(container)
                    manifest_path = os.path.join(containers_dir, f'{container}-pod.yaml')

                    with open(manifest_path, 'w') as f:
                        f.write(k8s_manifest)
                        logging.info(f'Kubernetes манифест для {container} создан: {manifest_path}')

                    subprocess.run(['kubectl', 'apply', '-f', manifest_path])
                    logging.info(f'Kubernetes манифест для {container} применен.')

        logging.info('Все манифесты применены.')
