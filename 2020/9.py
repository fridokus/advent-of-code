#!/usr/bin/python3

with open('9.in') as f:
    v = [int(i) for i in f]

for i in range(25, len(v)):
    if not v[i] in {x + y for x in v[i-25:i] for y in v[i-25:i] if x != y}: break

print(v[i])

k = 2
for j in range(len(v)):
    while sum(v[j:k]) < v[i]: k += 1
    if sum(v[j:k]) == v[i]: break

print(max(v[j:k]) + min(v[j:k]))
