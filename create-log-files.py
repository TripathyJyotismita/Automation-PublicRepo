#!/usr/bin/env python3

###################################################################################
# Script Name	: get-ssh-key.py
# Description	: Called by update-sshkey.yml to add user key.
# Args          :
# Author       	: Jyotismita Tripathy
# Email         : jyotismita.tripathy@oracle.com
# v1            : on 20-May-2020, Initial Draft
###################################################################################
import os, sys, logging, getpass
from datetime import datetime
whoAmI = getpass.getuser()
log_dir = "/tmp/script-logs/"
if os.path.isdir(log_dir):
    print('Log directory already present: ' + log_dir)
    pass
else:
    os.makedirs(os.path.dirname(log_dir))

log_filename = os.path.join(log_dir,whoAmI + datetime.now().strftime('-add-user-key-%H%M%d%m%Y.log'))
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=log_filename,
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)
#file_handler = logging.FileHandler(log_filename, mode="w", encoding=None, delay=False)
