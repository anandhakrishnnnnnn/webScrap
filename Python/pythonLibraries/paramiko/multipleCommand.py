import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip=input("Enter the IP : ").strip()
name=input("Enter the name : ").strip()
passwrd=input("Enter the password: ").strip()

client.connect(hostname=ip, username=name, password=passwrd)

commands="ls -l && whoami"

stdin, stdout, stderr = client.exec_command(commands)
print(stdout.read().decode())

client.close()  
