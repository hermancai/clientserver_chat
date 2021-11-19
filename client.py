import socket
import struct

SERVER = "localhost"
PORT = 3001

# create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
clientSocket.connect((SERVER, PORT))
print("Connected to %s port:%d" % (SERVER, PORT))
print("Type /q to quit")
print("Enter a message to send...")

# loop until user enters "/q"
while True:
	# get userInput from user
	userInput = input("CLIENT: ")
	encodedInput = userInput.encode()
	
	# send length of input
	inputLength = struct.pack(">i", len(encodedInput))
	while inputLength:
		inputLength = inputLength[clientSocket.send(inputLength):]

	# send input
	while encodedInput:
		encodedInput = encodedInput[clientSocket.send(encodedInput):]

	# quit program
	if userInput == "/q":
		break

	# get length of data to receive
	bytesToReceive = 4
	dataLength = b""
	while bytesToReceive > 0:
		tempBuffer = clientSocket.recv(1024)
		bytesToReceive -= len(tempBuffer)
		dataLength += tempBuffer
	dataLength = struct.unpack(">i", dataLength)[0]

	# receive data
	dataReceived = b""
	while dataLength > 0:
		tempBuffer = clientSocket.recv(1024)
		dataLength -= len(tempBuffer)
		dataReceived += tempBuffer
	dataReceived = dataReceived.decode()
	print("SERVER:", dataReceived)

clientSocket.close()
