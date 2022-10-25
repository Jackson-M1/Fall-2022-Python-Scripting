#!/usr/bin/env python3

'''
Author: Jackson Mckenney
Description: Week 9 Functions Lab
'''

def convert_temp(degreesF):
    return (degreesF - 32) * 5/9

def main():
    print(convert_temp(32))

if __name__ == "__main__":
    main()