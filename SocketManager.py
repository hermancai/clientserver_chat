import socket
import struct

class SocketManager:
	"""
	Class to hold functions used by both the client and server.

	Methods: 
		getHost()
		getPort()
		setSocket()
		sendData()
		receiveData()
	"""
	def __init__(self):
		self.host = "localhost"
		self.port = 3000
		self.socket = None

	def getHost(self) -> str:
		return self.host

	def getPort(self) -> int:
		return self.port

	def setSocket(self, socket: socket.socket):
		self.socket = socket

	def sendData(self, data: str):
		# turn string into bytes object
		encodedData = data.encode()

		"""
		SOURCE: inserting data length to the front of data string
		https://docs.python.org/3/howto/sockets.html
		https://docs.python.org/3/library/struct.html#format-strings
		"""
		# pack input length as 4-byte integer
		inputLength = struct.pack(">i", len(encodedData))

		# send splices of bytes object until empty
		while inputLength:
			inputLength = inputLength[self.socket.send(inputLength):]
		while encodedData:
			encodedData = encodedData[self.socket.send(encodedData):]

	def receiveData(self) -> str:
		"""
		SOURCE: looping recv
		https://docs.python.org/3/howto/sockets.html
		"""

		# data length is held in 4-byte integer
		bytesToReceive = 4
		dataLength = b""

		# loop until 4 bytes have been received
		while bytesToReceive > 0:
			tempBuffer = self.socket.recv(1024)
			# recv() returns empty byte string if connection closed
			if tempBuffer == b"":
				return ""
			bytesToReceive -= len(tempBuffer)
			dataLength += tempBuffer

		# unpack received bytes object as an integer
		dataLength = struct.unpack(">i", dataLength)[0]

		# buffer to hold data
		dataReceived = b""

		# loop to recv data until buffer size == dataLength
		while dataLength > 0:
			tempBuffer = self.socket.recv(1024)
			dataLength -= len(tempBuffer)
			dataReceived += tempBuffer
		dataReceived = dataReceived.decode()

		return dataReceived
