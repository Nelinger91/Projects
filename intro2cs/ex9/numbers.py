def scoreboard(num,sum = 0):
	newSum = num+sum
	return newSum

def isFinished(sum):
	if sum>=30:
		return True
	else:
		return False

def checkValid(string):
	if (string == "1" or string == "2" or string == "3" or string == "4"  or string == "5" or string == "6" or string == "7" or string == "8" or string == "9" or string == 1 or string == 2 or string == 3 or string == 4 or string == 5 or string == 6 or string ==7 or string == 8 or string == 9):
				return True
	elif string == "quit" or string == "QUIT":
		return ("close socket")
	else:
		return False

def updatePlayers(num):
	return num-1