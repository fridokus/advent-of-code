#!/usr/bin/python3

with open('8.in') as f:
    ins, nodes = f.read().split('\n\n')

n = len(ins)
nodes = {i[:3]: (i[7:10], i[12:15]) for i in nodes.splitlines()}
loc = 'AAA'

i = 0
while loc != 'ZZZ':
    loc = nodes[loc][0] if ins[i%n] == 'L' else nodes[loc][1]
    i += 1
print(i)
