import paramiko

client=paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('test.rebex.net',username="demo",password="password")

commands="whoami && ls"

    
stdin,stdout,stderr=client.exec_command(commands)

output=stdout.read().decode()
error=stderr.read().decode()

with open("output.txt","w") as out:
    out.write(output)
    
with open("errors.txt","w") as err:
    err.write(error)

client.close()