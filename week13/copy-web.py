#!/usr/bin/env python3

'''
Author: Jackson Mckenney
Description: week 11 interacting with a website lab
'''

import requests

response = requests.get("https://notpurple.com")

with open("my_web_file.html","w") as hFile:
    hFile.write(response.text)