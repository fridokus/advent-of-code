#!/usr/bin/python3

with open('13.in') as f:
    arrival = int(next(f))
    ids = next(f).strip().split(',')

ids = [0 if id == 'x' else int(id) for id in ids]
departure = arrival
while not any([not departure % id for id in ids if id]): departure += 1
print((departure - arrival) * max([id for id in ids if id and not departure % id]))

incr, t = 1, 0
for dt, id in zip([ids.index(i) for i in ids if i], [i for i in ids if i]):
    while (dt + t) % id: t += incr
    incr *= id
print(t)
