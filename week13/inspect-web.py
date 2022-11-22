#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

res = requests.get("https://notpurple.com")
soup = BeautifulSoup(res.text,'html.parser')

for link in soup.find_all('a'):
    print(f"{link.text}:  {link.get('href')}")