#! /usr/bin/env python3
data = open('6.in').read().splitlines()
operands = [[j for j in i.split(' ') if j] for i in data[:-1]]
ops = [i for i in data[-1].split(' ') if i]

r1 = 0
for i, op in enumerate(ops): r1 += eval(f' {op} '.join([operands[j][i] for j in range(len(operands))]))

print(r1)

r2 = 0
h = len(data)
ns = []
op = ''
for i in range(len(data[0]) - 1, -1, -1):
    new_n = ''
    for j in range(h):
        if not data[j][i]: continue
        if data[j][i] in ['*', '+']:
            op = data[j][i]
        else:
            new_n += data[j][i]
    if new_n.strip():
        ns.append(new_n)
    if op:
        r2 += eval(f' {op} '.join(ns))
        ns = []
        op = ''

print(r2)

