

# from paramiko import SSHClient
# import paramiko

# try:
#     client = paramiko.client.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('192.168.200.142',
#                     username='loko',
#                     password='4linux',
#                     port='22')

# except Exception as e:
#     print(f'Erro conexão: {e}')
#     exit

# stdin, stdout, stderr = client.exec_command('')
# if stdout.channel.recv_exit_status() == 0:
#     print(stdout.read().decode('utf-8'))
# else:
#     print(sterr.read().decode('utf-8'))


from paramiko import SSHClient
import paramiko

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname='192.168.200.142',username='loko',password='4linux')

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            print(stdout.read())

if __name__ == '__main__':
    ssh = SSH()
    ssh.exec_cmd("ls -l")