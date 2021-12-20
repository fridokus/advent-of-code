with open('20.in') as f:
    algo, lines = f.read().split('\n\n')

algo = algo.replace('#', '1').replace('.', '0')
lines = lines.splitlines()

real_size = len(lines[0])
size = real_size + 102
diff_by_2 = (size - real_size) // 2

def adjacent(m, j, i):
    if j == 0 or i == 0 or j == size-1 or i == size-1: return m[j][i]*9
    ret = ''
    for y in range(j-1, j+2): ret += ''.join([m[y][x] for x in range(i-1, i+2)])
    return ret

image = []
border = ['0' for i in range(diff_by_2)]
for _ in range(diff_by_2): image.append(['0' for i in range(size)])
for line in lines: image.append(border + list(line.replace('#', '1').replace('.', '0')) + border)
for _ in range(diff_by_2): image.append(['0' for i in range(size)])

def enhance(image):
    new_image = [[None for i in range(size)] for j in range(size)]
    for j in range(size):
        for i in range(size):
            new_image[j][i] = algo[int(adjacent(image, j, i), 2)]
    return new_image

for _ in range(2): image = enhance(image)
print(sum([sum([int(i) for i in line]) for line in image]))

for _ in range(48): image = enhance(image)
print(sum([sum([int(i) for i in line]) for line in image]))
