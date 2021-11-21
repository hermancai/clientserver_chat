import socket
from SocketManager import SocketManager


def main():
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
	displayPrompt = True

	# loop until user enters "/q" or connection is closed
	while True:
		# get response from client
		dataReceived = sm.receiveData()
		if not dataReceived:
			print("Client disconnected")
			break
		print("CLIENT:", dataReceived)

		# show message after getting first response from client
		if displayPrompt:
			print("Type /q to quit")
			displayPrompt = False

		# get non-empty input from user
		userInput = ""
		while not userInput:
			userInput = input("SERVER: ")

		# exit if specified
		if userInput == "/q":
			break

		# send data to client
		sm.sendData(userInput)
		
	conn.close()


if __name__ == "__main__":
	main()
