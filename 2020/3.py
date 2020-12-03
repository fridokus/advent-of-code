#!/usr/bin/python3

with open('3.in') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
h = len(lines)
w = len(lines[0])
y = 0
x = 0 

res1 = 0

while y < h - 1:
    y += 1
    x = (x + 3) % w
    res1 += lines[y][x] == '#'

print(res1)
