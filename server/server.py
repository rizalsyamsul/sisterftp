from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

ip = "localhost" #tinggal diganti ip server nanti
port = 9999
server = SimpleXMLRPCServer((ip,port), logRequests=True)

#fungsi untuk melihat list direktori
def list_directory():
    dir = os.getcwd()
    return os.listdir(dir)
server.register_function(list_directory, 'ls')

#fungsi untuk menerima upload dari client
def up(data,name):
    try:
        with open(name, "wb") as handle:
            f = data.data
            handle.write(f)
            return True
    except Exception as e:
        print(e)
server.register_function(up, 'Upload')

#fungsi untuk mengirim data ke client
def down(name):
    try:
        with open(name, "rb") as handle:
            return xmlrpc.client.Binary(handle.read())
            handle.close()
    except Exception as e:
        print(e)
server.register_function(down, 'Download')



if __name__ == '__main__':
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
