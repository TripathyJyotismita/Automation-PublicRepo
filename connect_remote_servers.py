
import paramiko
import time
HOST="138.1.157.1" #public ip of dbsystems/node

def connect_dbsystem(HOST):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=HOST, port=22, username='opc', password='')
        time.sleep(10)
        print('connection established!')
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Connection failed")
       
connect_dbsystem(HOST)
