with open('18.in') as f:
    lines = [list(i) for i in f.read().splitlines()]

not_numbers = ('[', ']', ',')

def explode(i, l):
    for x in range(i-2, -1, -1): 
        if l[x] not in not_numbers:
            l[x] = str(int(l[x]) + int(l[i]))
            break
    for y in range(i+3, len(l)):
        if l[y] not in not_numbers:
            l[y] = str(int(l[y]) + int(l[i+2]))
            break
    return l[:i-1] + ['0'] + l[i+4:]

def check_explode(l):
    depth = 0
    for i in range(len(l)):
        if depth == 5: return True, explode(i, l)
        if   l[i] == '[': depth += 1
        elif l[i] == ']': depth -= 1
    return False, l

def split(l):
    for i in range(len(l)):
        if l[i] not in not_numbers and int(l[i]) >= 10:
            x = str(int(l[i]) // 2)
            y = str((int(l[i]) + 1) // 2)
            l = l[:i] + ['['] + [x] + [','] + [y] + [']'] + l[i+1:]
            return True, l
    return False, l
    
def add(l1, l2): return ['['] + l1 + [','] + l2 + [']']

def magnitude(l):
    if type(l) == int: return l
    return 3 * magnitude(l[0]) + 2 * magnitude(l[1])

def add_all(lines):
    l = lines[0]
    for l2 in lines[1:]:
        l = add(l, l2)
        while True:
            did_explode = True
            while did_explode:
                did_explode, l = check_explode(l)
            did_split, l = split(l)
            if not did_split: break
    return l

l = eval(''.join(add_all(lines)))

print(magnitude(l))

r2 = 0
for l1 in lines:
    for l2 in lines:
        l = eval(''.join(add_all([l1, l2])))
        r2 = max(magnitude(l), r2)

print(r2)
