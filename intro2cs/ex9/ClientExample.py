#!python3
'''Example of a client program'''
import socket

HOST = 'river'    # The remote host
PORT = 5000      # The same port as used by the server
BUFF_SIZE = 1024
s = socket.socket()
s.connect(('river', 5000))
print('Connect to host', HOST)
str_msg = input('What do you want to tell the server?')
msg = bytes(str_msg, 'utf-8') # decode str in utf-8
s.sendall(msg) # Send bytes to the host
data = s.recv(BUFF_SIZE)
s.close()
print('Received', data)
