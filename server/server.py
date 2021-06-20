from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import os

ip = "26.229.87.196" #tinggal diganti ip server nanti
port = 9999
server = SimpleXMLRPCServer((ip,port), logRequests=True, allow_none=True)
# rh = RequestHandler(SimpleXMLRPCRequestHandler)


class Akun:
  def __init__(self, hostname, ip): # inisialisasi kelas
    self.hostname = hostname
    self.ip = ip
    self.jumlahup = 0
    self.jumlahdown = 0

arr_jml = []

def rankUp(array):
	return sorted(array, reverse=True, key = lambda  x: x['jml_up'])

def rankDwn(array):
	return sorted(array, reverse=True, key = lambda  x: x['jml_dwn'])


def add_akun(ip_address):
    global jml
    global arr_jml
    jml["ip"] = ip_address
    arr_jml.append(jml)
server.register_function(add_akun, 'ak')

def cek_upload():
    global jml
    print("Client IP : ",jml["ip"])
    print("jumlah upload : ",jml["jml_up"])
    print("jumlah download : ",jml["jml_dwn"])
server.register_function(cek_upload, 'cu')


#fungsi untuk melihat list direktori
def list_directory():
    dir = os.getcwd()
    return os.listdir(dir)
server.register_function(list_directory, 'ls')

#fungsi untuk menerima upload dari client
def up(data,name, hostname, ip_address):
    try:
        global jml
        global arr_jml
        if ip_address == jml["ip"]:
            with open(name, "wb") as handle:
                f = data.data
                handle.write(f)
                jml["jml_up"] += 1
                arr_jml.append(jml)
                return True
    except Exception as e:
        print(e)
server.register_function(up, 'Upload')

#fungsi untuk mengirim data ke client
def down(name, hostname, ip_address):
    try:
        global jml
        global arr_jml
        if ip_address == jml["ip"]:
            jml["jml_dwn"] += 1
            arr_jml.append(jml)
            with open(name, "rb") as handle:
                return xmlrpc.client.Binary(handle.read())
                handle.close()
    except Exception as e:
        print(e)
server.register_function(down, 'Download')

def rank():
    global jml
    global arr_jml
    topU = rankUp(arr_jml)[0]["ip"]
    up = rankUp(arr_jml)[0]["jml_up"]
    print("Client Dengan Upload Terbanyak: ",topU)
    print("Dengan Upload : ",up)
    topD = rankDwn(arr_jml)[0]["ip"]
    dwn = rankDwn(arr_jml)[0]["jml_dwn"]
    print("Client Dengan Download Terbanyak: ",topD)
    print("Dengan Download : ",dwn)
server.register_function(rank, 'rank')



if __name__ == '__main__':
    try:
        jml = {
            "ip": "",
            "jml_up": 0,
            "jml_dwn": 0
        }
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
