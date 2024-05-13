import paramiko
from scp import SCPClient


def tohost(host, user, passw, frm, to):
    global scp
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=passw)
        scp = SCPClient(ssh.get_transport())
        ssh.exec_command('rm -rf {}'.format(to))
        scp.put(frm, recursive=True, remote_path=to)
    finally:
        scp.close()
        ssh.close()


tohost('localhost', 'ubuntubob', '7492', 'C:/PycharmProjects/neurologix',
       '/home/ubuntubob')
