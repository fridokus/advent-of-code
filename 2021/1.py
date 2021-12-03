#!/usr/bin/python3

with open('1.in') as f:
    lines = [int(i) for i in f]

print(sum([lines[i+1] > lines[i] for i in range(len(lines) - 1)]))
print(sum([lines[i+3] > lines[i] for i in range(len(lines) - 3)]))
