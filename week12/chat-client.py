#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: week 12 sockets lab chat-client.py
'''

import socket

while 1:
    RHOST = '127.0.0.1'
    RPORT = 5000
    SND_DATA = input("Input message to send or 'exit' to exit: ")
    RCV_DATA = ""
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if SND_DATA == 'exit': 
        break
    else:
        C_SOCK.connect((RHOST,RPORT))
        C_SOCK.send(bytearray(SND_DATA, "utf-8"))
        RCV_DATA = C_SOCK.recv(1024)
        print(f"Data received back: {RCV_DATA.decode()}\n")

C_SOCK.close()
