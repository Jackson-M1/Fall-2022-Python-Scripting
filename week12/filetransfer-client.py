#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: week 12 sockets lab filetransfer-client.py
'''

import socket

with open("original.txt", "r") as originalFile:
    originalText = originalFile.read()
RHOST = '127.0.0.1'
RPORT = 5000
SND_DATA = originalText
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST,RPORT))
C_SOCK.send(bytearray(SND_DATA, "utf-8"))
C_SOCK.close()