from xmlrpc.client import ServerProxy
import xmlrpc.client
import xmlrpc.client as xmlrpclib
import os

proxy = ServerProxy('http://localhost:9999') #tinggal diganti ip server nanti


#fungsi untuk upload
def up_file(name):
    print("Uploading {}".format(name))
    try:
        with open(name, "rb") as handle:
            dt = xmlrpclib.Binary(handle.read())
            proxy.Upload(dt, name)
    except Exception as e:
        print(e)

#fungsi untuk download
def down_file(name):
    print("Downloading: {}".format(name))
    try:
        with open(name, "wb") as handle:
            dt = proxy.Download(name).data
            handle.write(dt)
            handle.close()
    except Exception as e:
        print(e)


while True:
    print('Menu FTP')
    print('1.download 2.upload 3.isi server 4.quit')
    print("pilih menu: ")
    temp = int(input())
    if temp == 1:
        print("file yang ada di server:")
        print(proxy.ls())
        print("file yang akan di akan di download dari server: ")
        file = input()
        down_file(file)
    elif temp == 2:
        print("file yang ada di client:")
        dir = os.getcwd()
        print(os.listdir(dir))
        print("file yang akan di upload: ")
        file = input()
        up_file(file)
    elif temp == 3:
        print(proxy.ls())
    elif temp == 4:
        break
