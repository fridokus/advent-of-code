#!/usr/bin/python3

from functools import reduce

with open('11.in') as f:
    inputs = [i.splitlines() for i in f.read().split('\n\n')]

class Monkey:
    def __init__(s, op, mod, true_target, false_target, items):
        s.op = op
        s.mod = mod
        s.true_target = true_target
        s.false_target = false_target
        s.items = items
        s.inspected = 0

    def __call__(s, div, monkeys):
        while s.items:
            s.inspected += 1
            old = s.items.pop(0)
            new = eval(s.op)
            if div: new //= 3
            new %= global_mod
            if not new % s.mod: monkeys[s.true_target ].items.append(new)
            else:                  monkeys[s.false_target].items.append(new)

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
    for m in monkeys: m(True, monkeys)
print(mul(*sorted([m.inspected for m in monkeys])[-2:]))

for round in range(10000):
    for m in monkeys2: m(False, monkeys2)
print(mul(*sorted([m.inspected for m in monkeys2])[-2:]))
