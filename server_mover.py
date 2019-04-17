#!/usr/bin/python3
import paramiko

## define servers we want to connect to
usercreds =[{"un":"bender","ip":"10.10.2.3"},{"un":"fry","ip":"10.10.2.4."},{"un":"zoidberg","ip":"10.10.2.5"}]

## loop through the servers we want to connect to
for fc in usercreds:
	this_transport = paramiko.Transport(fc['ip'],22)
	this_transport.connect(username=fc['un'], password='alta3')
	stfp = paramiko.SFTPClient.from_transport(this_transport)

	## move mybash.sh to each server
	# sftp.put("mybash.sh", "/tmp/mybash.sh")
	# sftp.chmod('/tmp/mybash.sh', 0o777)

	## close sftp object
	# sftp.close()
	this_transport.close()

	sshsession = paramiko.SSHClient()
	mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

	sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	sshsession.connect(hostname=fc['ip'],username=fc['un'],pkey=mykey)

	## execute mybash.sh
	sshsession.exec_command('cd /tmp; chmod u+x mybash.sh; ./mybash.sh')

## cat both files

## close connections
sshsession.close()
this_transport.close()
