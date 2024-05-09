import paramiko


def remove(host, user, passw):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=passw)

        # Завершить все контейнеры Docker
        stdin, stdout, stderr = ssh.exec_command("docker stop $(docker ps -a -q)")
        print(stdout.read().decode())

        # Удалить все контейнеры Docker
        stdin, stdout, stderr = ssh.exec_command("docker rm $(docker ps -a -q)")
        print(stdout.read().decode())

        # Удалить все изображения Docker
        stdin, stdout, stderr = ssh.exec_command("docker rmi $(docker images -a -q)")
        print(stdout.read().decode())

    finally:
        ssh.close()


remove('192.168.31.131', 'debian', '7492')
