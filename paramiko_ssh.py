import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.2.182',
                   username="systebui", password="vtech@123")
stdin, stdout, stderr = ssh_client.exec_command('pwd')
print(stdout.read())
stdin, stdout, stderr = ssh_client.exec_command('cd /')
print(stdout.read())
stdin, stdout, stderr = ssh_client.exec_command('ls')
print(stdout.readlines())