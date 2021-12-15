#!/usr/bin/python3

with open('13.in') as f:
    dots, instructions = f.read().split('\n\n')
    dots = dots.splitlines()
    instructions = instructions.splitlines()

paper = set()
for dot in dots:
    dot = dot.split(',')
    paper.add((int(dot[0]), int(dot[1])))

for i in instructions:
    v = int(i[13:])
    new_paper = set()
    if i[11] == 'x':
        for dot in paper:
            if dot[0] > v: new_paper.add((2 * v - dot[0], dot[1])) 
            else:          new_paper.add(dot)
    else:
        for dot in paper:
            if dot[1] > v: new_paper.add((dot[0], 2 * v - dot[1])) 
            else:          new_paper.add(dot)
    paper = new_paper
    print(len(paper))

printable = [[' ' for i in range(40)] for j in range(6)]
for dot in paper: printable[dot[1]][dot[0]] = '#'
for line in printable: print(line)
