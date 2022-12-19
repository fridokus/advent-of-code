#!/usr/bin/python3

from re import findall
from collections import deque

with open('19.in') as f:
    blueprints = [tuple([l[i+1] for i in range(6)]) for l in [[int(i) for i in findall(r'\d+', line)] for line in f.read().splitlines()]]

def simulate(costs, time_limit):
    state = (0, 1, 0, 0, 0, 0, 0, 0, 0) # time, robots, resources
    visited = set()
    max_ore_cost = max(costs[:3] + (costs[4],))
    ret = 0
    queue = deque((state,))
    while queue:
        state = queue.pop()
        t, robots, resources = state[0], list(state[1:5]), list(state[5:])
        ret = max(ret, resources[-1])
        if t == time_limit: continue
        time_left = time_limit - t
        # if not resources[-1] and robots[2]*time_left + resources[2] + sum((i+1 for i in range(time_left+1))) < costs[5]: continue
        # if t >= 20 and not resources[-1]: continue

        if time_left * max_ore_cost < resources[0] + (time_left - 1)*robots[0]: resources[0] = time_left * max_ore_cost - (time_left - 1)*robots[0]
        if time_left * costs[3] < resources[1] + (time_left - 1)*robots[1]:     resources[1] = time_left * costs[3]     - (time_left - 1)*robots[1]
        if time_left * costs[5] < resources[2] + (time_left - 1)*robots[2]:     resources[2] = time_left * costs[5]     - (time_left - 1)*robots[2]

        if robots[0] > max_ore_cost: robots[0] = max_ore_cost
        if robots[1] > costs[3]:     robots[1] = costs[3]
        if robots[2] > costs[5]:     robots[2] = costs[5]


        state = (t, *robots, *resources)

        if state in visited: continue
        visited |= {state}

        queue.append((state[0]+1,) + state[1:5] + tuple([state[i] + state[i+4] for i in range(1, 5)]))
        if resources[0] >= costs[4] and resources[2] >= costs[5]:
            queue.append((t+1, *robots[:3], robots[3]+1, resources[0] - costs[4] + robots[0], resources[1] + robots[1], resources[2] - costs[5] + robots[2], resources[3] + robots[3]))
        else:
            if resources[0] >= costs[2] and resources[1] >= costs[3]:
                queue.append((t+1, *robots[:2], robots[2]+1, robots[3], resources[0] - costs[2] + robots[0], resources[1] - costs[3] + robots[1], resources[2] + robots[2], resources[3] + robots[3]))
            if resources[0] >= costs[1]:
                queue.append((t+1, robots[0], robots[1]+1, *robots[2:], resources[0] - costs[1] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3]))
            if resources[0] >= costs[0]:
                queue.append((t+1, robots[0]+1, *robots[1:], resources[0] - costs[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3]))
    return ret

r1 = 0
r2 = 1
for b, costs in enumerate(blueprints):
    if b <3:
        r2 *= simulate(costs, 32)
    r1 += (b+1) * simulate(costs, 24)

print(r1)
print(r2)
