from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import os

ip = "localhost" #tinggal diganti ip server nanti
port = 9999
server = SimpleXMLRPCServer((ip,port), logRequests=True)
# rh = RequestHandler(SimpleXMLRPCRequestHandler) 


class Akun:
  def __init__(self, hostname, ip): # inisialisasi kelas
    self.hostname = hostname
    self.ip = ip
    self.jumlahup = 0
    self.jumlahdown = 0

arrAkun = []

# def cariAkun(ip):
#     for i in range (len(arrAkun)):
#         if arrAkun[i].ip == ip:
#             return i
#             break
#     i = -1            
#     return i

def cek_upload():
#     # return arrAkun[cariAkun(ip_address)].jumlahup
    return x
server.register_function(cek_upload, 'cu')


#fungsi untuk melihat list direktori
def list_directory():
    dir = os.getcwd()
    return os.listdir(dir)
server.register_function(list_directory, 'ls')

#fungsi untuk menerima upload dari client
def up(data,name, hostname, ip_address):
    try:
        with open(name, "wb") as handle:
            # idx = cariAkun(ip_address)
            # if idx != -1:
            #     arrAkun[idx].jumlahup = arrAkun[idx].jumlahup +1
            # else:
            #     akunx = Akun(hostname,ip)
            #     arrAkun.append(akunx)
            f = data.data
            handle.write(f)
            # x += 1
            return True
    except Exception as e:
        print(e)
server.register_function(up, 'Upload')

#fungsi untuk mengirim data ke client
def down(name, hostname, ip_address):
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
        x = 0
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
