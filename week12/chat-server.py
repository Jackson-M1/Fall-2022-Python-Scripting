#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: week 12 sockets lab chat-server.py
'''

import socket

LHOST = ''
LPORT = 5000
RCV_DATA = ""
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while 1:
    L_SOCK.listen(1)
    L_CONN, L_ADDR = L_SOCK.accept()
    print("Connected by ", L_ADDR)
    while 1: 
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        print(f"Server received:  {RCV_DATA.decode()}")
        L_CONN.sendall(b"I, the Server, received this data: " + RCV_DATA)
    L_CONN.close()
