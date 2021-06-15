#server
import socket
import os

ip = "26.229.87.196"
port = 8086
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(10)

print("Server started")
print("Waiting for client request...")
