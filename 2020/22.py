#!/usr/bin/python3

decks = [[int(n) for n in i.splitlines()[1:]] for i in open('22.in').read().split('\n\n')]

while all(decks):
    c1, c2 = decks[0].pop(0), decks[1].pop(0)
    if c1 > c2: decks[0] += [c1, c2]
    else:       decks[1] += [c2, c1]

if decks[0]: print(sum(i * decks[0][-i] for i in range(1, 51)))
else:        print(sum(i * decks[1][-i] for i in range(1, 51)))
