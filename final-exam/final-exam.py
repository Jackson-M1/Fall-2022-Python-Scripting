#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: Python Scripting Fall 2022 Final Exam
'''

import argparse, requests, json, socket
from bs4 import BeautifulSoup

def get_response(URL):
    get = requests.get(URL)
    return get.text
    
def parse_string(URL):
    get = requests.get(URL)
    soup = BeautifulSoup(get.text,'html.parser')
    return f"{soup.h3.text[2::3]} Jackson"
    

def parse_header(URL):
    get = requests.get(URL)
    return get.headers['FALL2022-HEADER']

def parse_json(URL):
    get = requests.get(URL)
    jason = json.loads(get.text)
    for item in jason['Music And Books']:
        if item['title'] == 'The Shining':
            return item['publish_info']['publish_year']
        
def socket_client(server):
    HOST = (server)
    PORTS = (range(6100, 6201))
    SEND = "Jackson Mckenney"
    RCV = ""
    for port in PORTS:
        try:
            C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            C_SOCK.connect((HOST,port))
            C_SOCK.send(bytearray(SEND,'utf-8'))
            RCV = f"{C_SOCK.recv(1024).decode()} Port: {port}"
        except socket.error as e:
            pass
    C_SOCK.close()
    return RCV

parser = argparse.ArgumentParser(description="Python Scripting Fall 2022 Final Exam")
parser.add_argument('-s', '--server', dest='server', required=True, help="<required> Enter the server name 'www.py.land', or 'port.py.land' if 5 is entered for the question")
parser.add_argument('-q', '--question', dest='question', required=True, type=int, help='<required> Enter the number 1, 2, 3, 4, or 5')
args = parser.parse_args()

URL = (f"http://{args.server}/q{args.question}")

#chris = {1:get_response(URL),2:parse_string(URL),3:parse_header(URL),4:parse_json(URL),5:socket_client(args.server)}

print("Name: Jackson Mckenney")
print(URL)
if args.question == 1:
    print("ANSWER:", get_response(URL))
elif args.question == 2:
    print("ANSWER:", parse_string(URL))
elif args.question == 3:
    print("ANSWER:", parse_header(URL))
elif args.question == 4:
    print("ANSWER:", parse_json(URL))
elif args.question == 5:
    print("ANSWER:", socket_client(args.server))
else:
    print("Use './final-exam.py -h' for help")

# for key in chris:
#     if args.question == key:
#         print("ANSWER:", chris[key])
#     else: 
#         print("Use './final-exam.py -h' for help")