#!/usr/bin/python3

with open('24.in') as f:
    parts = [i.splitlines() for i in f.read().split('inp w')[1:]]

stack = []
for i, part in enumerate(parts):
    add = int(part[5][6:])
    if add > 0:
        stack.append((i, int(part[-3][6:])))
        continue
    show = stack.pop()
    add += show[1]
    print('decimal %d + %d = decimal %d' % (i, -1 * add, show[0]))
