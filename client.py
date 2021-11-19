import socket
from SocketManager import SocketManager


# set up client
sm = SocketManager()
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((sm.getHost(), sm.getPort()))
sm.setSocket(clientSocket)

print("Connected to %s port:%d" % (sm.getHost(), sm.getPort()))
print("Type /q to quit")
print("Enter a message to send...")

# loop until user enters "/q"
while True:
	# send user input to server
	userInput = input("CLIENT: ")
	sm.sendData(userInput)
	if userInput == "/q":
		break

	# get response from server
	dataReceived = sm.receiveData()
	if dataReceived == "/q":
		break
	print("SERVER:", dataReceived)

clientSocket.close()
