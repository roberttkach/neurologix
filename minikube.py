import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)


def generate_k8s_manifest(container_name, name):
    return f"""
apiVersion: v1
kind: Pod
metadata:
  name: {name}-{container_name}-pod
spec:
  containers:
  - name: {name}-{container_name}
    image: {name}-{container_name}:latest
"""


def process_container_dir(containers_dir, name):
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
                        try:
                            subprocess.run(['docker', 'inspect', f'{name}-{container}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                            logging.error(f'Контейнер с именем {name}-{container} уже существует.')
                        except subprocess.CalledProcessError:
                            subprocess.run(['docker', 'build', '-t', f'{name}-{container}:latest', container_path])

                            k8s_manifest = generate_k8s_manifest(container, name)
                            manifest_path = os.path.join(containers_dir, f'{name}-{container}-pod.yaml')

                            with open(manifest_path, 'w') as f:
                                f.write(k8s_manifest)
                                logging.info(f'Kubernetes манифест для {name}-{container} создан: {manifest_path}')

                            subprocess.run(['kubectl', 'apply', '-f', manifest_path])
                            logging.info(f'Kubernetes манифест для {name}-{container} применен.')

            logging.info('Все манифесты применены.')
