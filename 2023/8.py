#!/usr/bin/python3

from functools import reduce

with open('8.in') as f:
    ins, nodes = f.read().split('\n\n')

n = len(ins)
nodes = {i[:3]: (i[7:10], i[12:15]) for i in nodes.splitlines()}

def steps_to_z(loc):
    for i in range(10000000):
        loc = nodes[loc][0] if ins[i%n] == 'L' else nodes[loc][1]
        if loc[2] == 'Z': break
    return i+1

print(steps_to_z('AAA'))
print(reduce(lambda x, y: x*y, [steps_to_z(loc) // n for loc in {l for l in nodes if l[2] == 'A'}]) * n)
