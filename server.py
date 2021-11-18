import socket

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

# receive data and send response
response = conn.recv(4096)
print("Received from client:", response)
conn.send("Got data from client".encode())

conn.close()