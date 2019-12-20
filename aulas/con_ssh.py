import paramiko

try:
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramik.AutoAddPolicy())
    client.connect('192.168.200.142'),
                    username='loko',
                    password='4linux'
                    port='22'

except Exception as e:
    print(f'Erro conexão: {e}')
    exit

stdin, stdout, stderr = client.exec_command('')
if stdout.channel.recv_exit_status
