from xmlrpc.server import SimpleXMLRPCServer
import os

ip = "26.229.87.196"
port = 9999
server = SimpleXMLRPCServer((ip,port), logRequests=True)

def list_directory():
    dir = os.getcwd()
    return os.listdir(dir)
server.register_function(list_directory, 'ls')

def up():
    return 'uhuy'
server.register_function(up, 'Upload')

if __name__ == '__main__':
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')

