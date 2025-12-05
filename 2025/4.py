#! /usr/bin/env python3
G = {x+y*1j: c for x, r in enumerate(open('4.in')) for y, c in enumerate(r) if c != '\n'}
N = {x+y*1j for x in (-1,0,1) for y in (-1,0,1)} - {0}
adj = lambda p: sum(G.get(p+d) == '@' for d in N)
print(sum(G[p] == '@' and adj(p) < 4 for p in G))
sim = lambda: (dead := {p for p in G if G[p] == '@' and adj(p) < 4}) and \
              len(dead) + (G.update({p: '.' for p in dead}) or sim()) or 0
print(sim())
