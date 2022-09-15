#!/usr/bin/env python3
'''
Author: Jackson Mckenney
This is my script for the String Formatting lab
'''
varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295
print('')
print("Example Answer:")
print(f"Your {varGreen:<0s} Output\n")
print(f"1.\tHello {varName}")
print(f"2.\t{varRed}-{varGreen}-{varBlue}")
print(f"3.\tIs this {varGreen.lower()} or {varBlue.lower()}?")
print(f"4.\tMy name is {varName.upper()}")
print(f"5.\t[{varRed:+^7s}]")
print(f"6.\t[{varGreen.lower():=<7s}]")
print(f"7.\t[{varBlue.lower():*>9s}]")
print(f"8.\t{varBlue * 10}")
print(f"9.\t{varLoot}")
print(f"10.\t{varLoot:<.1f}")
print(f"11.\tI have ${varLoot:<.2f}")
print(f"12.\t[{varRed:$^10s}][{varGreen:$^10s}][{varBlue:$^10s}]")
print(f"13.\t[ {varRed[::-1]} ][{varGreen:^7s}][ {varBlue[::-1]} ]")
print(f"14.\tFirst Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
print('')