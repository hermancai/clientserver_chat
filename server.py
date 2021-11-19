import socket
import struct

SERVER = "localhost"
PORT = 3001

# create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((SERVER, PORT))

# listen for a client
serverSocket.listen(1)
print("Server listening on %s port:%d" % (SERVER, PORT))

# connect with client
conn, addr = serverSocket.accept()
print("Connected by", addr)
print("Waiting for message...")

while True:
	# get length of data to receive
	bytesToReceive = 4
	dataLength = b""
	while bytesToReceive > 0:
		tempBuffer = conn.recv(1024)
		bytesToReceive -= len(tempBuffer)
		dataLength += tempBuffer
	dataLength = struct.unpack(">i", dataLength)[0]

	# receive data
	dataReceived = b""
	while dataLength > 0:
		tempBuffer = conn.recv(1024)
		dataLength -= len(tempBuffer)
		dataReceived += tempBuffer
	dataReceived = dataReceived.decode()
	
	# quit program
	if dataReceived == "/q":
		break

	print("CLIENT:", dataReceived)

	# get userInput from user
	userInput = input("SERVER: ")
	encodedInput = userInput.encode()
	
	# send length of input
	inputLength = struct.pack(">i", len(encodedInput))
	while inputLength:
		inputLength = inputLength[conn.send(inputLength):]

	# send input
	while encodedInput:
		encodedInput = encodedInput[conn.send(encodedInput):]

	# quit program
	if dataReceived == "/q":
		break

conn.close()
