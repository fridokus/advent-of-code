#! /usr/bin/env python3
data = open('3.in').read().splitlines()
solve = lambda s, n: n and (m := max(s[:-n+1 or None])) + solve(s[s.find(m)+1:], n-1) or ''
[print(sum(int(solve(row, k)) for row in data)) for k in (2, 12)]
