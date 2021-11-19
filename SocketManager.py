import socket
import struct

class SocketManager:
	def __init__(self):
		self.host = "localhost"
		self.port = 3000
		self.socket = None

	def getHost(self):
		return self.host

	def getPort(self):
		return self.port

	def setSocket(self, socket: socket.socket):
		self.socket = socket

	def sendData(self, data: str):
		encodedData = data.encode()

		# pack input length as 4-byte integer
		inputLength = struct.pack(">i", len(encodedData))

		# send spliced data until string is empty
		# send length then data
		while inputLength:
			inputLength = inputLength[self.socket.send(inputLength):]
		while encodedData:
			encodedData = encodedData[self.socket.send(encodedData):]

	def receiveData(self) -> str:
		# data length is held in 4-byte integer
		bytesToReceive = 4
		dataLength = b""
		# loop until 4 bytes have been received
		while bytesToReceive > 0:
			tempBuffer = self.socket.recv(1024)
			bytesToReceive -= len(tempBuffer)
			dataLength += tempBuffer
		dataLength = struct.unpack(">i", dataLength)[0]

		# buffer to hold data
		dataReceived = b""
		# loop until buffer size = dataLength
		while dataLength > 0:
			tempBuffer = self.socket.recv(1024)
			dataLength -= len(tempBuffer)
			dataReceived += tempBuffer
		dataReceived = dataReceived.decode()
		return dataReceived
