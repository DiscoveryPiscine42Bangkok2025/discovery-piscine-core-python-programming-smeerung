#!/usr/bin/env python3

x = float(input("Give me a number: "))
if x%1 == 0:
    print(int(x))
else:
    print(int(x) + 1)