#!/usr/bin/python3

size = 6

def is_number_ok(n):
    l = list(map(int, str(n)))
    double = 0
    for i in range(1, size):
        if l[i] < l[i-1]:
            return 0
        if l[i] == l[i-1]:
            double_here = True
            if i > 1 and l[i-2] == l[i]:
                double_here = False
            if i < 5 and l[i+1] == l[i]:
                double_here = False
            double += double_here

    if double:
        return 1
    return 0


low = 171309
high = 643603

range_of_numbers = range(low, high+1)

hits = 0

for n in range_of_numbers:
    hit = is_number_ok(n)
    hits += hit

print(hits)
