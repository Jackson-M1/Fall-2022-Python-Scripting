#!/usr/bin/env python3
'''
Author: Jackson Mckenney
This script demonstrates my ability to slice strings and lists, as well as how to create for loops.
'''
varString = "Here is a nice string to slice"
varList = [ "Here", "is", "a", "nice", "list", "to", "slice" ]
print(varString[3:])
print(varString[0:3])
print(varString[3:12])
print(varString[::2])
print(varString[::-1])
print("")
print(varList[::-1])
print(varList[-5::-1])
print(varList[2:4])
print(varList[::3])
print(varList[1:])
print("")
for character in varString:
    print (character)
print("")
for string in varList:
    print (string)