#!/usr/bin/python3

with open('14.in') as f:
    operations = [i.replace(']', '').split(' = ') for i in f.read().splitlines()]

apply_mask = lambda v, mask: int(''.join([mask[i] if mask[i] != 'X' else v[i] for i in range(36)]), 2)
mem = {}
for op, v in operations:
    if op == 'mask': mask = v
    else: mem[int(op[4:])] = apply_mask(str(bin(int(v)))[2:].zfill(36), mask)

print(sum([v for k, v in mem.items()]))

def addresses(x):
    if not 'X' in x: yield x
    else:
        yield from addresses(x.replace('X', '0', 1))
        yield from addresses(x.replace('X', '1', 1))

mem = {}
for op, v in operations:
    if op == 'mask': mask = v
    else:
        a = str(bin(int(op[4:])))[2:].zfill(36)
        x = ''.join([mask[i] if mask[i] != '0' else a[i] for i in range(36)])
        for k in addresses(x): mem[int(k, 2)] = int(v)

print(sum([v for k, v in mem.items()]))
