#!/usr/bin/python3

with open('8.in') as f:
    lines = f.read().splitlines()

signals = []
outputs = []
r1 = 0
for line in lines:
    line = line.split(' | ')
    signals.append(line[0].split())
    outputs.append(line[1].split())
    r1 += sum([(2 <= len(i) <= 4) or len(i) == 7 for i in outputs[-1]])

print(r1)

r2 = 0
for signal, output in zip(signals, outputs):
    mapping = ['' for i in range(10)]
    signal = sorted(signal, key=len)
    for i in signal:
        if   len(i) == 2: mapping[1] = i
        elif len(i) == 3: mapping[7] = i
        elif len(i) == 4: mapping[4] = i
        elif len(i) == 5:
            if   all([c in i for c in mapping[1]]): mapping[3] = i
            elif sum([c in i for c in mapping[4]]) == 3: mapping[5] = i
            else: mapping[2] = i
        elif len(i) == 6:
            if   all([c in i for c in mapping[4]]): mapping[9] = i
            elif all([c in i for c in mapping[7]]): mapping[0] = i
            else: mapping[6] = i
        else: mapping[8] = i

    output_number = 0
    for j, n in enumerate(output[::-1]):
        for i in range(10):
            if all([c in n for c in mapping[i]]) and len(mapping[i]) == len(n):
                output_number += i * 10 ** j
                break

    r2 += int(output_number)

print(r2)
