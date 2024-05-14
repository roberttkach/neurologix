import os
import subprocess


containers_dir = "neurologix/containers"



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


for container in os.listdir(containers_dir):
    container_path = os.path.join(containers_dir, container)

    if os.path.isdir(container_path):
        dockerfile_path = os.path.join(container_path, 'Dockerfile')

        if os.path.exists(dockerfile_path):
            # Построение Docker образа
            subprocess.run(['docker', 'build', '-t', f'{container}:latest', container_path])

            # Генерация Kubernetes манифеста
            k8s_manifest = generate_k8s_manifest(container)
            manifest_path = os.path.join(containers_dir, f'{container}-pod.yaml')

            with open(manifest_path, 'w') as f:
                f.write(k8s_manifest)
                print(f'Kubernetes манифест для {container} создан: {manifest_path}')

            # Применение Kubernetes манифеста
            subprocess.run(['kubectl', 'apply', '-f', manifest_path])
            print(f'Kubernetes манифест для {container} применен.')

print('Все манифесты применены.')