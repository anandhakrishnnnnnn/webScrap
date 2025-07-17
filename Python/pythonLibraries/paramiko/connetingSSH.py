import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.1.27', username='anand', password='Anandhan@2007')

stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.read().decode())

client.close()
