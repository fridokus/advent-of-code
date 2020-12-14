#!/usr/bin/python3

with open('14.in') as f:
    operations = [i.replace(']', '').split(' = ') for i in f.read().splitlines()]

def apply_mask(v, mask):
    v = ['0' for i in range(36 - len(v))] + v
    return int(''.join([mask[i] if mask[i] != 'X' else v[i] for i in range(36)]), 2)

mem = [0 for i in range(100000)]
for op, v in operations:
    if op == 'mask': mask = list(v)
    else: mem[int(op[4:])] = apply_mask(list(bin(int(v)))[2:], mask)

print(sum(mem))

def yield_addresses(x):
    if not 'X' in x: yield x
    else:
        yield from yield_addresses(x.replace('X', '0', 1))
        yield from yield_addresses(x.replace('X', '1', 1))

mem = {}
for op, v in operations:
    if op == 'mask': mask = v
    else:
        a = list(bin(int(op[4:])))[2:]
        a = ['0' for i in range(36 - len(a))] + a
        x = ''.join([mask[i] if mask[i] != '0' else a[i] for i in range(36)])
        for k in yield_addresses(x): mem[int(k, 2)] = int(v)

print(sum([v for k, v in mem.items()]))
