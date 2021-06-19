#server
# import socket
# import os

# ip = "26.229.87.196"
# port = 8086
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((ip, port))
# server.listen(10)

# print("Server started")
# print("Waiting for client request...")

from xmlrpc.server import SimpleXMLRPCServer
import os

ip = "26.229.87.196"
port = 4899
server = SimpleXMLRPCServer((ip,port), logRequests=True)

def list_directory(dir):
    return os.listdir(dir)

server.register_function(list_directory, 'ls')

if __name__ == '__main__':
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')

