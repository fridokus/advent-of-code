#!/usr/bin/python3

with open('12.in') as f:
    rows = ((list(l.split()[0]), eval('(' + l.split()[1] + ')')) for l in f.read().splitlines())

for r in rows:
    pass
