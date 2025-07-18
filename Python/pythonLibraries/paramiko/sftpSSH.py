import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('test.rebex.net', username='demo', password='password')

sftp = client.open_sftp()

remote_file = '/pub/example/readme.txt'
local_path = 'ownloaded_readme.txt'

sftp.get(remote_file, local_path)

print(f"Downloaded {remote_file} to {local_path}")

sftp.close()
client.close()
