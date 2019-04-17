#!/usr/bin/python3

##import libraries
import os
import paramiko
import warnings

## excel data or csv data
excel_list=[{"un":"bender","ip":"10.10.2.3"},{"un":"fry","ip":"10.10.2.4"},{"un":"zoidberg","ip":"10.10.2.5"}]

## filter warnings
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

## We create an empty session:
sshsession = paramiko.SSHClient()

## Go grab an SSH key:
key1 = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## skips a new fingerprint warning:
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for fc in excel_list:
	## press the connect button in our putty session:
	sshsession.connect(hostname=fc['ip'], username=fc['un'], pkey=key1)

	## capture 3 responses from exec_command
	ssh_in, ssh_out, ssh_err = sshsession.exec_command('ls /var/')

	## display the results of the command
	print(ssh_out.read().decode('utf-8'))

	## ssh is not a barn
	sshsession.close()
