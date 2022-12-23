#!/usr/bin/python3

with open('23.in') as f:
    scan = f.read().splitlines()

elves = [] # list of elf = [(pos x y), (proposal)]
positions = set()
for j in range(len(scan)):
    for i in range(len(scan[0])):
        if scan[j][i] == '#':
            elves.append([(i, j), (i, j)])
            positions |= {(i, j)}

dirs = {
        'N': [(-1, -1), ( 0, -1), ( 1, -1)],
        'S': [(-1,  1), ( 0,  1), ( 1,  1)],
        'W': [(-1,  1), (-1,  0), (-1, -1)],
        'E': [( 1,  1), ( 1,  0), ( 1, -1)]
        }
order = ['N', 'S', 'W', 'E']
for r in range(10000):
    moved = False
    blocklist = set()
    proposals = set()
    for elf in elves:
        p = elf[0]
        # check if no neighbor
        if all([all([(p[0] + dirs[d][i][0], p[1] + dirs[d][i][1]) not in positions for d in order]) for i in range(3)]):
            continue
        for d in order:
            if all([(p[0] + dirs[d][i][0], p[1] + dirs[d][i][1]) not in positions for i in range(3)]):
                proposal = (p[0] + dirs[d][1][0], p[1] + dirs[d][1][1])
                if proposal in proposals:
                    blocklist |= {proposal}
                else:
                    proposals |= {proposal}
                    elf[1] = proposal
                moved = True
                break
    for elf in elves:
        if elf[1] not in blocklist:
            elf[0] = elf[1] # move to proposal
        else:
            elf[1] = elf[0] # reset proposal to position
    order = order[1:] + [order[0]]
    positions = {elf[0] for elf in elves}
    if r == 9:
        xpos = {elf[0][0] for elf in elves}
        ypos = {elf[0][1] for elf in elves}
        r1 = (max(ypos) - min(ypos) + 1) * (max(xpos) - min(xpos) + 1) - len(positions)
        print(r1)
    if not moved: break
print(r+1)
