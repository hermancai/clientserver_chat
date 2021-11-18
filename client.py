import socket

SERVER = "localhost"
PORT = 3001

# create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
clientSocket.connect((SERVER, PORT))
print("Connected to %s port:%d" % (SERVER, PORT))

# send data and get response
clientSocket.send("Hello".encode())
response = clientSocket.recv(4096)
print(response)

clientSocket.close()