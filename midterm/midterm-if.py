#!/usr/bin/env python3

'''
Author: Jackson Mckenney
Description: Midterm part 1 - If
'''

print("Name: Jackson Mckenney")

# Total = 0
# lineNum = 0
# with open("Midterm-if.txt","r") as ifFile:
#     for line in ifFile:
#         if "gmeach18@ed.gov" in line:
#             Total += lineNum
#         elif "248.253.63.149" in line:
#             Total += lineNum
#         elif "Whiteland" in line:
#             Total += lineNum
#         elif "80.222.19.190" in line:
#             Total += lineNum
#         elif "Kayley" in line:
#             Total += lineNum
#         elif "dcassyqw@microsoft.com" in line:
#             Total += lineNum
#         lineNum += 1
            
           
#print(f"The total is: {Total}")

# Total = 0
# lineNum = 0
# ifFile = open("Midterm-if.txt","r")
# ifContent = ifFile.readline()
# while ifContent:
#     ifContent = ifFile.readline()
#     lineNum += 1
#     if "gmeach18@ed.gov" in ifContent:
#         Total += lineNum
#     elif "248.253.63.149" in ifContent:
#         Total += lineNum
#     elif "Whiteland" in ifContent:
#         Total += lineNum
#     elif "80.222.19.190" in ifContent:
#         Total += lineNum
#     elif "Kayley" in ifContent:
#         Total += lineNum
#     elif "dcassyqw@microsoft.com" in ifContent:
#         Total += lineNum
# ifFile.close()
# print(f"The total is: {Total}")

Total = 0
ifFile = open("Midterm-if.txt","r")
ifContent = ifFile.readline()
while ifContent:
    ifContent = ifFile.readline()
    if "gmeach18@ed.gov" in ifContent:
        Total += int(ifContent[0:2])
    elif "248.253.63.149" in ifContent:
        Total += int(ifContent[0:3])
    elif "Whiteland" in ifContent:
        Total += int(ifContent[0:2])
    elif "80.222.19.190" in ifContent:
        Total += int(ifContent[0:3])
    elif "Kayley" in ifContent:
        Total += int(ifContent[0:3])
    elif "dcassyqw@microsoft.com" in ifContent:
        Total += int(ifContent[0:3])
ifFile.close()
print(f"The total is: {Total}")