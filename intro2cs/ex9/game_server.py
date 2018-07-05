import socket
import sys
import numbers


HOST = socket.gethostname()
PORT = int(sys.argv[1])
num_of_players=int(sys.argv[3])
socket_list=[]
s=socket.socket()
s.bind((HOST, PORT))
s.listen(0)

error = "TEXT ERROR bad input. try again"
byteGO = bytes ("GO", 'utf-8')
byteError = bytes (error, 'utf-8')
newSum = 0
win = "TEXT You win!"
byteWin = bytes (win, 'utf-8')
print ("Waiting for client connections")


for i in range(num_of_players):
	connection, address=s.accept()
	msg = "TEXT Welcome to the game"
	bytemsg =  bytes(msg,'utf-8')
	connection.send(bytemsg)
	socket_list.append(connection)


run = True
while run == True:
	for i in range(num_of_players):
		turn = "TEXT sum is %d enter number" %newSum
		byteTurn = bytes (turn, 'utf-8')
		num_of_errors = 0
		socket_list[i].send(byteTurn)
		socket_list[i].send(byteGO)
		socket_list[i].settimeout(10)
		data = socket_list[i].recv(1024)
		decodeData = data.decode('utf-8')
		if decodeData[:4]!= "MOVE":
			socket_list[i].close()
			socket_list.pop(i)
		good = numbers.checkValid(decodeData[4:])
		if good == "close socket":
			socket_list.pop(i)
			decodeData = "quit"
			num_of_players -= 1
			if num_of_players == 1:
				socket_list[0].send(byteWin)
				check == True
		while good == False:
			num_of_errors += 1
			if num_of_errors<5:
				socket_list[i].send(byteError)
				socket_list[i].send(byteGO)
				newdata = socket_list[i].recv(1024)
				decodeData = newdata.decode('utf-8')
				good = numbers.checkValid(decodeData[4:])
			else:
				socket_list[i].close()
				socket_list.pop(i)
				good = True
				decodeData = "5 errors"
				num_of_players -= 1
				if num_of_players == 1:
					socket_list[0].send(byteWin)
					check == True
		if decodeData!="5 errors" and decodeData != "quit":
			newSum = numbers.scoreboard(int(decodeData[4:]), newSum)
			check = numbers.isFinished(newSum)
		if check==True:
			socket_list[i].send(byteWin)
			s.close()
			run = False
			break







