#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: Week 14 JSON lab
'''

import json, requests, argparse

parser = argparse.ArgumentParser(description="Enter an ip address to retreive its information")

parser.add_argument('--ipaddress', dest='ip', required=True, help='<required> Enter an ip address')
args = parser.parse_args()

res = requests.get(f"http://ipinfo.io/{args.ip}/json")
myDict = json.loads(res.text)

if res.status_code != 404:
    for key,value in myDict.items():
        print(key,":",value)
else:
    print(myDict['error']['message'])
    