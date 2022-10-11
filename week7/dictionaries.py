#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: Learning how to use dictionaries
'''
dict = {"server1.testlab.com":"192.168.1.10",
        "server2.testlab.com":"192.168.1.11",
        "server3.testlab.com":"192.168.1.12",
        "server4.testlab.com":"192.168.1.13",
        "server5.testlab.com":"192.168.1.14",
        "server6.testlab.com":"192.168.1.15"
        }
print(f"Keys: {dict.keys()}\n")
print(f"Values: {dict.values()}\n")
print(f"Items: {dict.items()}\n")

dict["server7.testlab.com"] = "192.168.1.16"
dict["server8.testlab.com"] = "192.168.1.17"

if "server2.testlab.com" in dict:
    print("server2.testlab.com is contained in dict\n")
else:
    print("server2.testlab.com not found\n")

if "server10.testlab.com" in dict:
    print("server10.testlab.com is contained in dict\n")
else:
    print("server10.testlab.com not found\n")
