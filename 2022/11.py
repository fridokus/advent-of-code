#!/usr/bin/python3

import re
from functools import reduce

with open('11.in') as f:
    inputs = [i.splitlines() for i in f.read().split('\n\n')]

class Monkey:
    def __init__(self, op, mod, true_target, false_target, items):
        self.items = items
        self.op = op
        self.mod = mod
        self.true_target = true_target
        self.false_target = false_target
        self.inspected = 0

    def turn(self, div):

        while self.items:
            self.inspected += 1
            old = self.items.pop(0)
            new = self.op(old)
            if div: new //= 3

            new %= global_mod
            if not new % self.mod: monkeys[self.true_target ].items.append(new)
            else:                  monkeys[self.false_target].items.append(new)

monkeys = []
ops = [lambda x: x*7, lambda x: x+7, lambda x: x*3, lambda x: x+3, lambda x: x*x, lambda x: x+8, lambda x: x+2, lambda x: x+4]
for i, m in enumerate(inputs):
    items = list(map(int, re.findall(r'\d+', m[1])))
    op = ops[i]
    mod = int(m[3][21:])
    true_target = int(m[4][29])
    false_target = int(m[5][30])
    monkeys.append(Monkey(op, mod, true_target, false_target, items))

global_mod = reduce(lambda x, y: x*y, [m.mod for m in monkeys])
for round in range(20):
    for i, monkey in enumerate(monkeys):
        monkey.turn(div=True)

l = sorted([m.inspected for m in monkeys])
r2 = l[-1] * l[-2]
print(r2)

monkeys = []

for i, m in enumerate(inputs):
    items = list(map(int, re.findall(r'\d+', m[1])))
    op = ops[i]
    mod = int(m[3][21:])
    true_target = int(m[4][29])
    false_target = int(m[5][30])
    monkeys.append(Monkey(op, mod, true_target, false_target, items))

for round in range(10000):
    for i, monkey in enumerate(monkeys):
        monkey.turn(div=False)

l = sorted([m.inspected for m in monkeys])
r2 = l[-1] * l[-2]
print(r2)
