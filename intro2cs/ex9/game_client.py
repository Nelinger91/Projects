import socket
import sys

HOST = sys.argv[2]
PORT = int(sys.argv[3])
client = socket.socket()
client.connect((HOST, PORT))
welcome = client.recv(1024)
decodeWelcome=welcome.decode('utf-8')
print (decodeWelcome[5:])
while True:
	data = client.recv(1024)
	decodeData = data.decode('utf-8')
	if decodeData[:4]=="TEXT":
		print (decodeData[5:])
	if decodeData[-2:] == "GO" or decodeData == "GO":
		move = input('')
		movebytes = bytes("MOVE"+move,'utf-8')
		client.sendall(movebytes)
	if decodeData[5:] == "You win!":
		client.close()



