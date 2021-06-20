from xmlrpc.client import ServerProxy
import xmlrpc.client
import xmlrpc.client as xmlrpclib
import os
import time

proxy = ServerProxy('http://localhost:9999') #tinggal diganti ip server nanti


#fungsi untuk upload
def up_file(name):
    print("Uploading {}".format(name))
    try:
        with open(name, "rb") as handle:
            ip = handle.address_string()
            dt = xmlrpclib.Binary(handle.read())
            proxy.Upload(dt, name, ip)
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nSelamat Datang di Salty Spitton \n Apakah anda ingin connect? \n 1. Ya \n 2. Tidak")
    temp = int(input())
    if temp == 1:
        print("Berhasil menjalin koneksi")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print('\nMenu FTP')
            print(' 1.download \n 2.upload \n 3.isi server \n 4.quit')
            print("pilih menu: ")
            temp2 = int(input())
            if temp2 == 1:
                print("file yang ada di server:")
                print(proxy.ls())
                print("file yang akan di akan di download dari server: ")
                file = input()
                down_file(file)
            elif temp2 == 2:
                print("file yang ada di client:")
                dir = os.getcwd()
                print(os.listdir(dir))
                print("file yang akan di upload: ")
                file = input()
                up_file(file)
            elif temp2 == 3:
                print(proxy.ls())
            elif temp2 == 4:
                break
        
    elif temp == 2:
        break
    else:
        print('Pilihan Salah')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
