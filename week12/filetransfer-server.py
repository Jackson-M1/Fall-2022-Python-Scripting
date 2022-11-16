#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: week 12 sockets lab filetransfer-server.py
'''

import socket

LHOST = ''
LPORT = 5000
RCV_DATA = ""
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

L_SOCK.listen(1)
L_CONN, L_ADDR = L_SOCK.accept()
print("Connected by ", L_ADDR)
RCV_DATA = L_CONN.recv(1024)
print("Server stored file contents as newfile.txt")
with open("newfile.txt", "w") as newFile:
    newFile.write(RCV_DATA.decode())
L_CONN.close()
