from xmlrpc.client import ServerProxy
import os

proxy = ServerProxy('http://26.229.87.196:9999')

if __name__ == '__main__':
    while True:    
        print('Menu FTP')
        print('/n 1.download 2.upload 3.isi server 4.quit')
        temp = input("pilih menu: ")
        if temp == 1:
            print('download')
        elif temp == 2:
            print(proxy.Upload())
        elif temp == 3:
            print(proxy.ls())
        elif temp == 4:
            break