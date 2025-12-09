#! /usr/bin/env python3
import math as m, itertools as t, collections as c
P = [list(map(int, x.split(','))) for x in open('8.in')]; N = len(P)
E = sorted((sum((a-b)**2 for a,b in zip(P[i], P[j])), i, j) for i, j in t.combinations(range(N), 2))
F = lambda i, u: i if u[i] == i else (u.__setitem__(i, F(u[i], u)) or u[i])
u = list(range(N)); [u.__setitem__(F(i, u), F(j, u)) for _, i, j in E[:(10, 1000)[N>50]]]
print(m.prod(sorted(c.Counter(F(i, u) for i in range(N)).values())[-3:]))
u, k = list(range(N)), [N]; print(next(P[i][0]*P[j][0] for _, i, j in E if (r:=F(i, u))!=(R:=F(j, u)) and not (u.__setitem__(r, R) or k.__setitem__(0, k[0]-1)) and k[0]==1))
