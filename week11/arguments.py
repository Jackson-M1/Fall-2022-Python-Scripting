#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: Week 11 argparse lab
'''

import argparse

parser = argparse.ArgumentParser(description="This is Jackson Mckenney's script")

parser.add_argument('-m', dest='basic', help='Enter some text')
parser.add_argument('-i', '--integer', dest='int', metavar='[an integer]', required=True, type=int, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', dest='float', metavar='[a float]', type=float, help='Enter a simple float')
parser.add_argument('-s', '--string', dest='string', metavar='[a string]', help='Enter a simple string')
parser.add_argument('-l', dest='list', metavar='[strings]', nargs='+', help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='setTrue', default=False, action='store_true', help='Toggle from default False to True')
parser.add_argument('-f', '--setfalse', dest='setFalse', default=True, action='store_false', help='Toggle from default True to False')
parser.add_argument('-v', '--version', dest='version', action='version', version='%(prog)s 2.0', help="show program's version number and exit")

args = parser.parse_args()
print("Integer: ",args.int)
print("String: ",args.string)
print("Float: ",args.float)
print("List: ",args.list)