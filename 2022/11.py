#!/usr/bin/python3

from functools import reduce

with open('11.in') as f:
    inputs = [i.splitlines() for i in f.read().split('\n\n')]

class Monkey:
    def __init__(self, op, mod, true_target, false_target, items):
        self.op = op
        self.mod = mod
        self.true_target = true_target
        self.false_target = false_target
        self.items = items
        self.inspected = 0

    def turn(self, div, monkeys):
        while self.items:
            self.inspected += 1
            old = self.items.pop(0)
            new = eval(self.op)
            if div: new //= 3
            new %= global_mod
            if not new % self.mod: monkeys[self.true_target ].items.append(new)
            else:                  monkeys[self.false_target].items.append(new)

monkeys  = []
monkeys2 = []
for i, m in enumerate(inputs):
    items  = eval('[' + m[1][18:] + ']')
    op = m[2][19:]
    mod = int(m[3][21:])
    true_target = int(m[4][29])
    false_target = int(m[5][30])
    monkeys .append(Monkey(op, mod, true_target, false_target, items))
    monkeys2.append(Monkey(op, mod, true_target, false_target, items[:]))

mul = lambda x, y: x*y
global_mod = reduce(mul, [m.mod for m in monkeys])
for round in range(20):
    for m in monkeys: m.turn(True, monkeys)
print(mul(*sorted([m.inspected for m in monkeys])[-2:]))

for round in range(10000):
    for m in monkeys2: m.turn(False, monkeys2)
print(mul(*sorted([m.inspected for m in monkeys2])[-2:]))
