#!/usr/bin/env python3

import f2c

fahrenheit = float(input("Input a temperature to be converted to celsius: "))
print(f2c.convert_temp(fahrenheit))