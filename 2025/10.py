#! /usr/bin/env python3
import re

L = open('10.in').read().splitlines()
P = [(1 if c=='#' else 0 for c in re.search(r'\[([#\.]+)\]', s).group(1)) for s in L]
B = [[[int(x) for x in p.split(',')] for p in re.findall(r'\(([\d,]+)\)', s)] for s in L]
J = [[int(x) for x in re.search(r'\{([\d,]+)\}', s).group(1).split(',')] for s in L]

solve1 = lambda t, btns: min((bin(m).count('1') for m in range(1<<len(btns))
    if [sum((m>>b&1) and (k in btns[b]) for b in range(len(btns)))%2 for k in range(len(list(t)))] == list(t)), default=0)
print(sum(solve1(list(t), b) for t, b in zip(P, B)))

def solve2(btns, tgt, sol=[]):
    if all(x==0 for x in tgt): return sum(sol)
    if any(x<0 for x in tgt) or len(sol) >= len(btns): return float('inf')
    limit = min((tgt[r]//1 for r in btns[len(sol)] if btns[len(sol)]), default=50)
    return min((solve2(btns, [t - k*(i in btns[len(sol)]) for i, t in enumerate(tgt)], sol+[k])
               for k in range(limit + 1)), default=float('inf'))

print(sum(solve2(b, j) for b, j in zip(B, J)))
