#!/usr/bin/python3

from re import findall
from collections import defaultdict
from itertools import combinations

with open('16.in') as f:
    lines = f.read().splitlines()

valid_targets = set()
distances = defaultdict(dict)
flow_rates = dict()
n_lines = len(lines)

for line in lines:
    valve = line[6:8]
    rate = int(findall(r'\d+', line)[0])
    if rate:
        valid_targets |= {valve}
        flow_rates[valve] = rate
    distances[valve][1] = set(line[49:].strip().split(', '))

for d in range(2, n_lines):
    for valve in distances:
        distances[valve][d] = set()
        for target in distances[valve][d-1]:
            targets_of_target = set()
            for target_of_target in distances[target][1]:
                seen = any([target_of_target in distances[valve][i] for i in range(1, d)]) or target_of_target == valve
                if not seen: targets_of_target.add(target_of_target)
            distances[valve][d] |= targets_of_target

max_distance = 0
for valve in distances:
    for d in range(1, n_lines):
        distances[valve][d] &= valid_targets
        if distances[valve][d]: max_distance = max(max_distance, d)

class State:
    def __init__(self, pos='AA', just_moved=False, open_valves=set(), t=0, score=0, visited=set()):
        self.pos = pos
        self.just_moved = just_moved
        self.open_valves = open_valves
        self.t = t
        self.score = score
        self.visited = visited

    def add_flow_to_score(self):
        for valve in self.open_valves:
            self.score += flow_rates[valve]


states = [State()]
idle_final_per_pos = defaultdict(int)
states26 = []
while True == True:
    if min([state.t for state in states]) >= 30: break
    for state in states:
        idle_final_here = 0
        for valve in state.open_valves:
            idle_final_here += flow_rates[valve] * (30 - state.t)
        if state.t > 3 and idle_final_here + state.score <= idle_final_per_pos[state.pos]:
            states.remove(state)
            continue
        if state.t >= 30: continue
        if state.t == 26:
            new_state = State(pos=state.pos, just_moved=state.just_moved, open_valves=state.open_valves.copy(), t=state.t, score=state.score, visited=state.visited.copy())
            states26.append(new_state)
        state.add_flow_to_score()
        if state.just_moved:
            state.open_valves |= {state.pos}
            state.just_moved = False
            state.t += 1
            continue

        if not valid_targets - state.open_valves or state.t >= 22: # tiral and error :/ TODO: copy state and step t when above a certain value
            state.t += 1
            continue

        for d in range(1, max_distance+1):
            if not distances[state.pos][d]: continue
            new_t = state.t + d
            if new_t >= 30: continue
            for target in distances[state.pos][d]:
                if target in state.visited: continue
                new_state = State(pos=target, just_moved=True, open_valves=state.open_valves.copy(), t=new_t, score=state.score, visited=state.visited.copy() | {target})
                for _ in range(d-1): new_state.add_flow_to_score()
                states.append(new_state)

        states.remove(state)

print(max([state.score for state in states]))
r2 = 0
for s1, s2 in combinations(states26, 2):
    if not s1.visited & s2.visited:
        r2 = max(r2, s1.score + s2.score)
print(r2)
