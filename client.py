import socket
from SocketManager import SocketManager


def main():
	# set up client
	sm = SocketManager()
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect with server
	clientSocket.connect((sm.getHost(), sm.getPort()))
	sm.setSocket(clientSocket)

	print("Connected to %s port:%d" % (sm.getHost(), sm.getPort()))
	print("Type /q to quit")
	print("Enter a message to send...")

	# loop until user enters "/q" or connection is closed
	while True:
		# get non-empty input from user
		userInput = ""
		while not userInput:
			userInput = input("CLIENT: ")
		
		# exit if specified
		if userInput == "/q":
			break

		# send data to server
		sm.sendData(userInput)
		
		# get response from server
		dataReceived = sm.receiveData()
		if not dataReceived:
			print("Server disconnected")
			break
		print("SERVER:", dataReceived)

	clientSocket.close()


if __name__ == "__main__":
	main()
