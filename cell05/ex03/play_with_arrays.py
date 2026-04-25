#!/usr/bin/env python3

num = [2, 8, 9, 48, 8, 22, -12, 2]
x = num[0]

two = [i + x for i in num if i > 5]
unique_list = list(set(two))
print(unique_list)