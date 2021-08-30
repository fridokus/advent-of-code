#!/usr/bin/python3

changes = [int(i) for i in open('1.in').read().splitlines()]
print(sum(changes))

visited = set()
i = 0
ptr = 0

while i not in visited:
    visited.add(i)
    i += changes[ptr]
    ptr = (ptr + 1) % len(changes)

print(i)
