#!/usr/bin/python3

with open('1.in') as f:
    lines = f.read().splitlines()

elves = [0]
for line in lines:
    if line: elves[-1] += int(line)
    else: elves += [0]

print(max(elves))

r2 = 0
for _ in range(3):
    r2 += max(elves)
    elves.remove(max(elves))
print(r2)
