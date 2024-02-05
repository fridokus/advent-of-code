#!/usr/bin/python3

from re import findall

with open('12.in') as f:
    rows = ((list(l.split()[0]), eval('(' + l.split()[1] + ')')) for l in f.read().splitlines())

def variations(r):
    for i in range(len(r)):
        if r[i] == '?':
            yield from variations(r[:i] + ['.'] + r[i+1:])
            yield from variations(r[:i] + ['#'] + r[i+1:])
            break
    else: yield r

print(sum([sum([tuple(map(len, findall(r'#+', ''.join(v)))) == r[1] for v in variations(r[0])]) for r in rows]))
