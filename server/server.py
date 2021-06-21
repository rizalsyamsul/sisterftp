#server
#import library
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

#Inisiasi Server
ip = "26.229.87.196"
port = 9999
server = SimpleXMLRPCServer((ip,port), logRequests=True, allow_none=True)

#Fungsi tambahan untuk penghitungan dalam fungsi utama
#fungsi untuk mencari akun
def searchakun(ip):
    global arr_ip
    i = 0
    while True:
        if ip == arr_ip[i]['ip']:
            idx = i
            break
        i += 1
    return idx

#fungsi untuk mencari upload terbanyak dalam array
def mostUpload(arr):
	return sorted(arr, reverse=True, key = lambda  x: x['up'])

#fungsi untuk mencari download terbanyak dalam array
def mostDownload(arr):
	return sorted(arr, reverse=True, key = lambda  x: x['down'])

#Fungsi Utama
#fungsi untuk menambah akun saat pertama login , terdapat inf yg berisi ip, total upload, total download
def add_akun(ip_address):
    global inf
    inf = {"ip": "","up": 0,"down": 0}
    inf["ip"] = str(ip_address)
    arr_ip.append(inf)
    print("IP: {} connected as client".format(ip_address))
server.register_function(add_akun, 'ak')

#fungsi untuk melihat list direktori dalam server
def list_directory():
    dir = os.getcwd()
    return os.listdir(dir)
server.register_function(list_directory, 'ls')

#fungsi untuk menerima upload dari client
def up(data,name,ip_address):
    try:
        global arr_ip
        ip = str(ip_address)
        idx = searchakun(ip)
        if ip == arr_ip[idx]["ip"]:
            with open(name, "wb") as handle:
                f = data.data
                handle.write(f)
                arr_ip[idx]["up"] += 1
                print("Add: {} from client".format(name))
                return True
        else:
            print('wrong ip')
    except Exception as e:
        print(e)
server.register_function(up, 'Upload')

#fungsi untuk mengirim data ke client
def down(name, ip_address):
    try:
        global arr_ip
        ip = str(ip_address)
        idx = searchakun(ip)
        if ip == arr_ip[idx]["ip"]:
            arr_ip[idx]["down"] += 1
            print("Sending: {} to client".format(name))
            with open(name, "rb") as handle:
                return xmlrpc.client.Binary(handle.read())
                handle.close()
        else:
            print('wrong ip')
    except Exception as e:
        print(e)
server.register_function(down, 'Download')

#fungsi untuk mengecek upload dan download dari client yang dipilih
def cek_updown(ip_address):
    global arr_ip
    ip = str(ip_address)
    idx = searchakun(ip)
    if ip == arr_ip[idx]["ip"]:
        print("Client IP : ",arr_ip[idx]["ip"])
        print("jumlah upload : ",arr_ip[idx]["up"])
        print("jumlah download : ",arr_ip[idx]["down"])
    else:
        print('wrong ip')
server.register_function(cek_updown, 'cu')

#fungsi untuk mengetahui ip client mana yang memiliki download dan upload paling banyak
def rank():
    global arr_ip
    sort = mostUpload(arr_ip)
    ip_up = sort[0]["ip"]
    up = sort[0]["up"]
    print("IP Client Dengan Upload Terbanyak: ",ip_up)
    print("Dengan Total Upload : ",up)
    sort2 = mostDownload(arr_ip)
    ip_down = sort2[0]["ip"]
    down = sort2[0]["up"]
    print("IP Client Dengan Download Terbanyak: ",ip_down)
    print("Dengan Total Download : ",down)
server.register_function(rank, 'rank')

#main fuction
if __name__ == '__main__':
    try:
        arr_ip = []
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
