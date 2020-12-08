#!/usr/bin/python3

with open('1.in') as f:
    lines = f.readlines()
    lines = [int(i.strip()) for i in lines]
    l = len(lines)

print([x * y for x in lines for y in lines if x + y == 2020][0])
print([x * y * z for x in lines for y in lines for z in lines if x + y + z == 2020][0])
