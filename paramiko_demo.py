#!/usr/bin/python3

##import standard libraries
import os
import paramiko

## We create an empty session:
sshsession = paramiko.SSHClient()

## Go grab an SSH key:
key1 = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## skips a new fingerprint warning:
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## press the connect button in our putty session:
sshsession.connect(hostname='10.10.2.3',username='bender',pkey=mykey)

## capture 3 responses from exec_command
ssh_in, ssh_out, ssh_err = sshsession.exec_command('ls /var/')

## display the results of the command
print(ssh_out.read().decode('utf-8'))
