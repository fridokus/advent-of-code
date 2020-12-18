#!/usr/bin/python3
import re

with open('18.in') as f:
    lines = f.read().splitlines()

res1 = 0
for line in lines:
    p = int(len(line) / 4.5)
    for c in '()': line = line.replace(c, c * p)
    line = re.sub(r'(\d)', r'\1)', line)
    line = '(' * (line.count(')') - line.count('(')) + line
    res1 += eval(line)

print(res1)

class Int2(int):
    def __mul__(self, i):
        return Int2(int(self) + i)

    def __add__(self, i):
        return Int2(int(self) * i)

res2 = 0
for line in lines:
    line = re.sub(r'(\d)', r'Int2(\1)', line)
    line = line.replace('*', 'X').replace('+', '*').replace('X', '+')
    res2 += eval(line)

print(res2)
