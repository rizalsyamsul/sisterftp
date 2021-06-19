#client
# import socket
# import os

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# isconnect = False
# print('Menu FTP')
# print('/n 1.download 2.upload 3.isi server 3.quit')
# while True:
#     if(isconnect == False):
#         print('Connect To Server First')
#         print('Connectting To Server...')
#         client.connect("26.229.87.196", 8086)
#         isconnect = True
#         if isconnect == True:
#             print("Connected \n")
#         else:
#             print("Failed to Connect.\n")
#     else:
#         temp = input("pilih menu: ")
#         if temp == 1:
#             print('download')
#         elif temp == 2:
#             print('upload')
#         elif temp == 3:
#             print('data')
        

from xmlrpc.client import ServerProxy
import os

proxy = ServerProxy('http://26.229.87.196:9999')

if __name__ == '__main__':
    dr = os.getcwd()
    print(proxy.ls(dr))