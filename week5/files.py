#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: Interacting with file data using different read functions
'''
passwd = open("/etc/passwd", "r")
passwdContent = passwd.read()
print(len(passwdContent))
print("length for read represents the number of characters")
print("You use this read function (read) when you want to work with the entire file at once and have it output as a string.\n")
passwd.close()

passwd1 = open("/etc/passwd", "r")
passwd1Content = passwd1.readlines()
print(len(passwd1Content))
print("length for readlines represents the number of lines")
print("You use this read function (readlines) when you want to run through a list and do something with each line one at a time, this read function outputs each line seperately in a list.\n")
passwd1.close()

passwd2 = open("/etc/passwd", "r")
passwd2line = passwd2.readline()
passwd2Content = passwd2line
while passwd2line:
    passwd2line = passwd2.readline()
    passwd2Content += passwd2line
totalChar = len(passwd2Content)
print(totalChar)
print("You use this read function (readline + loop) when you want to process the file one line at a time and do the same thing to each line of the file.")
passwd2.close()