import time

with open('19.in') as f:
    scans = [[eval('(' + j + ')') for j in i.splitlines()[1:]] for i in f.read().split('\n\n')]

def orientations(v):
    for i in rotations(v): yield from spins(i)

def spins(v): # barrel roll
    yield v
    yield (v[0], -v[2], v[1])
    yield (v[0], -v[1], -v[2])
    yield (v[0], v[2], -v[1])

def rotations(v): # backflip and 360
    yield v
    yield (v[2], v[1], -v[0])
    yield (-v[0], v[1], -v[2])
    yield (-v[2], v[1], v[0])
    yield (v[1], -v[0], v[2])
    yield (-v[1], v[0], v[2])
    
def check_match(diffs1, diffs2):
    matches = set(diffs1) & set(diffs2)
    if len(matches) >= 11: return matches.pop()

points = scans[0]
translations = []
dones = [0 for i in range(len(scans[1:]))]
while True == True:
    for k, scan in enumerate(scans[1:]):
        if dones[k]: continue
        diffs_points_v  = [[ tuple(points[i][x] -  points[j][x] for x in range(3)) for i in  range(len(points)) if i != j] for j in  range(len(points))]
        for oriented_scanner in zip(*(orientations(i) for i in scan)):
            matches = 0
            diffs_scanner_v = [[tuple(oriented_scanner[i][x] - oriented_scanner[j][x] for x in range(3)) for i in range(len(oriented_scanner)) if i != j] for j in range(len(oriented_scanner) - 10)]
            translation = None
            for i, diffs_points in enumerate(diffs_points_v):
                for j, diffs_scanner in enumerate(diffs_scanner_v):
                    matching_diff = check_match(diffs_points, diffs_scanner)
                    if matching_diff:
                        translation = tuple(points[i][x] - oriented_scanner[j][x] for x in range(3))
                        dones[k] = 1
                        break
                if translation: break
            if translation:
                translations.append(translation)
                for v in oriented_scanner:
                    candidate = tuple(v[x] + translation[x] for x in range(3))
                    if candidate not in points: points.append(candidate)
                break
    print(dones)
    if all(dones): break

print(len(points))

r2 = 0
for translation1 in translations:
    for translation2 in translations:
        r2 = max(r2, sum([abs(translation1[i] - translation2[i]) for i in range(3)]))
    
print(r2)
