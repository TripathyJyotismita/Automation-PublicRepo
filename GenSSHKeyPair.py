import os
import sys
import subprocess
from pathlib import Path

CUR_USER = os.getlogin()
PLATFORM = sys.platform

if PLATFORM == "win32":
    PRIV_SSH_DIR = "C:\\Users\\%s\\.ssh" % (CUR_USER)
elif PLATFORM == "linux":
    PRIV_SSH_DIR = "/home/%s/.ssh" % (CUR_USER)

def generate_keys():
    home = str(Path.home())
    dir_name = '.ssh'

    if os.path.isdir((SSH_DIR)):
        printInfo("{} already present".format(SSH_DIR))
        pass
    else:
        os.mkdir((home + '/' + dir_name))

    printInfo('gen key cmd to be executed')
    cmd = os.system(
        ("ssh-keygen -t rsa -N '' -b 2048 -f {}'id_rsa' ").format(SSH_DIR))

    pubKeys = [line.strip() for line in (open((os.path.join(SSH_DIR + 'id_rsa.pub'))))]
    return pubKeys
    
   
  if os.path.isdir(SSH_DIR) == False:
            printInfo("Your key file is not set!! We are creating your ssh key! ")
            pubKeys = generate_keys()
            printInfo('generating key pair!!')
   
