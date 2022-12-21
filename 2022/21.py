#!/usr/bin/python3

with open('21.in') as f:
    lines = f.read().splitlines()

monkeys = {}
while 'root' not in monkeys:
    for line in lines:
        m = line[:4]
        if len(line) > 8: m1, m2 = line[6:10], line[13:]
        try:
            if   '+' in line: monkeys[m] = monkeys[m1] +  monkeys[m2]
            elif '-' in line: monkeys[m] = monkeys[m1] -  monkeys[m2]
            elif '*' in line: monkeys[m] = monkeys[m1] *  monkeys[m2]
            elif '/' in line: monkeys[m] = monkeys[m1] // monkeys[m2]
            else:             monkeys[m] = int(line[6:])
        except (KeyError, TypeError): pass

print(monkeys['root'])

for line in lines: monkeys[line[:4]] = line[6:]
del monkeys['humn']
equation = monkeys.pop('root').replace('+', '=')
while any([k in equation for k in monkeys]):
    for m in monkeys:
        if m in equation:
            equation = equation.replace(m, '(' + monkeys[m] + ')')

equation = equation.replace('=', '- (') + ')'
c = eval(equation.replace('humn', '-1j'))
r2 = round(c.real / c.imag)
print(r2)
