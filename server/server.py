from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import os

ip = "26.229.87.196" #tinggal diganti ip server nanti
port = 9999
server = SimpleXMLRPCServer((ip,port), logRequests=True, allow_none=True)

def rankUp(array):
	return sorted(array, reverse=True, key = lambda  x: x['up'])

def rankDwn(array):
	return sorted(array, reverse=True, key = lambda  x: x['down'])

def searchakun(arr_ip,ip):
    i = 0
    while True:
        if ip == arr_ip[i]['ip']:
            idx = i
            break
        i += 1
    return idx

def add_akun(ip_address):
    global inf
    global arr_ip
    inf["ip"] = ip_address
    arr_ip.append(inf)
server.register_function(add_akun, 'ak')


def cek_upload(ip_address):
    global inf
    global arr_ip
    idx = searchakun(arr_ip,ip_address)
    if ip_address == arr_ip[idx]["ip"]:
        print("Client IP : ",arr_ip[idx]["ip"])
        print("jumlah upload : ",arr_ip[idx]["up"])
        print("jumlah download : ",arr_ip[idx]["down"])
    else:
        print('wrong ip')
server.register_function(cek_upload, 'cu')


#fungsi untuk melihat list direktori
def list_directory():
    dir = os.getcwd()
    return os.listdir(dir)
server.register_function(list_directory, 'ls')

#fungsi untuk menerima upload dari client
def up(data,name, hostname, ip_address):
    try:
        global inf
        global arr_ip
        if ip_address == inf["ip"]:
            with open(name, "wb") as handle:
                f = data.data
                handle.write(f)
                idx = searchakun(arr_ip,ip_address)
                arr_ip[idx]["up"] += 1
                return True
    except Exception as e:
        print(e)
server.register_function(up, 'Upload')

#fungsi untuk mengirim data ke client
def down(name, hostname, ip_address):
    try:
        global inf
        global arr_ip
        idx = searchakun(arr_ip,ip_address)
        if ip_address == arr_ip[idx]["ip"]:
            arr_ip[idx]["down"] += 1
            with open(name, "rb") as handle:
                return xmlrpc.client.Binary(handle.read())
                handle.close()
        else:
            print('wrong ip')
    except Exception as e:
        print(e)
server.register_function(down, 'Download')

def rank():
    global inf
    global arr_ip
    topU = rankUp(arr_ip)[0]["ip"]
    up = rankUp(arr_ip)[0]["up"]
    print("Client Dengan Upload Terbanyak: ",topU)
    print("Dengan Upload : ",up)
    topD = rankDwn(arr_ip)[0]["ip"]
    dwn = rankDwn(arr_ip)[0]["down"]
    print("Client Dengan Download Terbanyak: ",topD)
    print("Dengan Download : ",dwn)
server.register_function(rank, 'rank')

if __name__ == '__main__':
    try:
        arr_ip = []
        inf = {"ip": "","up": 0,"down": 0}
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
