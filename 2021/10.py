#!/usr/bin/python3

with open('10.in') as f:
    lines = f.read().splitlines()

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
closers = {'(': ')', '[': ']', '{': '}', '<': '>'}

r1 = 0
incomplete = []
for line in lines:
    state = []
    for char in line:
        if char in closers:
            state.append(char)
        elif char != closers[state.pop()]:
            r1 += points[char]
            break
    else:
        incomplete.append(state)

print(r1)

points = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []
for line in incomplete:
    score = 0
    while line:
        score = score * 5 + points[closers[line.pop()]]
    scores.append(score)

print(sorted(scores)[len(scores)//2])
