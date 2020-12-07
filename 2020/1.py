#!/usr/bin/python3

with open('1.in') as f:
    lines = f.readlines()
    lines = [int(i.strip()) for i in lines]
    l = len(lines)

print(max([max([x * y if x + y == 2020 else 0 for x in lines]) for y in lines]))
print(max([max([max([x * y * z if x + y + z == 2020 else 0 for x in lines]) for y in lines]) for z in lines]))
