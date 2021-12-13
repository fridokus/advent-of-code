from collections import defaultdict

with open('12.in') as f:
    start_end = [line.split('-') for line in f.read().splitlines()]

connections = defaultdict(set)
for start, end in start_end:
    connections[start].add(end)
    connections[end].add(start)

def a(visited, path): return False
def b(visited, path): return path != 'start' and not any([visited.count(i) > 1 and i.islower() for i in visited])

def paths(visited, part):
    if visited[-1] == 'end': yield 1
    else:
        for path in connections[visited[-1]]:
            if path.isupper() or path not in visited or part(visited, path):
                yield from paths(visited + [path], part)

print(sum(paths(['start'], a)))
print(sum(paths(['start'], b)))
