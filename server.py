import socket
from SocketManager import SocketManager


# set up server
sm = SocketManager()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((sm.getHost(), sm.getPort()))

# listen for a client
serverSocket.listen(1)
print("Server listening on %s port:%d" % (sm.getHost(), sm.getPort()))

# connect with client
conn, addr = serverSocket.accept()
sm.setSocket(conn)
print("Connected by", addr)
print("Waiting for message...")

# loop until user enters "/q"
while True:
	# get response from client
	dataReceived = sm.receiveData()
	if dataReceived == "/q":
		break
	print("CLIENT:", dataReceived)

	# send user input to client
	userInput = input("SERVER: ")
	sm.sendData(userInput)
	if userInput == "/q":
		break

conn.close()
