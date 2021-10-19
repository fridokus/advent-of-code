#!/usr/bin/env python3

name = input("Specify name (which in-file to be used):")
file_name = "1_%s.in" % name if name else "1.in"
changes = [int(i) for i in open(file_name).read().splitlines()]
print(sum(changes))

visited = set()
i = 0
ptr = 0

while i not in visited:
    visited.add(i)
    i += changes[ptr]
    ptr = (ptr + 1) % len(changes)

print(i)
