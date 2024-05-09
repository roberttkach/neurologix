import os
import paramiko
from scp import SCPClient


def tohost(host, user, passw, frm, to):
    global scp
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=passw)
        scp = SCPClient(ssh.get_transport())
        remote_path = os.path.join(to, os.path.basename(frm)).replace("\\", "/")
        ssh.exec_command('rm -rf {}'.format(remote_path))
        scp.put(frm, recursive=True, remote_path=remote_path)
    finally:
        scp.close()
        ssh.close()


tohost('192.168.31.131', 'debian', '7492', r'C:\Users\diner\PycharmProjects\monitoring_ml\stream-data-machine',
       '/home/debian/github')
