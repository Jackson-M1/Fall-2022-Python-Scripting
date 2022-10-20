#!/usr/bin/env python3

'''
Author: Jackson Mckenney
Description: Midterm part 3 - Slicing
'''

print("Name: Jackson Mckenney")

with open("slicing-file.txt", "r") as slicingFile:
    slicingContent = slicingFile.readlines()
    a = " ".join(slicingContent[-3:-4:-1])
    b = " ".join(slicingContent[2:5])
    c = " ".join(slicingContent[-10:-15:-2])
    d = " ".join(slicingContent[10:13])
    e = " ".join(slicingContent[-19:-22:-1])
    quote = f"{a} {b} {c} {d} {e}".replace('\n','')
    print(quote)