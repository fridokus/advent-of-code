#!/usr/bin/python3

from functools import reduce
import math as m

with open('6.in') as f:
    lines = f.read().splitlines()

ts = [int(i) for i in lines[0][11:].split()]
ds = [int(i) for i in lines[1][11:].split()]
print(reduce(lambda x, y: x*y, [sum([h * (ts[i]-h) > ds[i] for h in range(ts[i])]) for i in range(len(ts))]))
print(2 * m.floor(m.sqrt((int(''.join([str(i) for i in ts]))/2)**2 - int(''.join([str(i) for i in ds])))))
