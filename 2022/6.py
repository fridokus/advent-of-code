#!/usr/bin/python3

with open('6.in') as f:
    s = f.read()

def find_m(s, l):
    for i in range(len(s)-l):
        if len(set(s[i:i+l])) == l: return i+l

print(find_m(s, 4))
print(find_m(s, 14))
