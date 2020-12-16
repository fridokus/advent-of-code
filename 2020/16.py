#!/usr/bin/python3
import re

with open('16.in') as f:
    notes = f.read().split('\n\n')

rules = re.findall(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', notes[0].replace('\n',''))
my_ticket = [int(i) for i in notes[1].splitlines()[1].split(',')]
nearby_tickets = [[int(i) for i in ticket.split(',')] for ticket in notes[2].splitlines()[1:]]

res1 = 0
discarded = []
for i, ticket in enumerate(nearby_tickets):
    for value in ticket:
        if all([(value < int(rule[1]) or value > int(rule[2])) and
            (value < int(rule[3]) or value > int(rule[4])) for rule in rules]):
            res1 += value
            discarded.append(i)

print(res1)

nearby_tickets = [ticket for i, ticket in enumerate(nearby_tickets) if i not in discarded]
can_be_l = []
for rule in rules:
    can_be = []
    for i in range(len(my_ticket)):
        if all([(ticket[i] >= int(rule[1]) and ticket[i] <= int(rule[2])) or
            (ticket[i] >= int(rule[3]) and ticket[i] <= int(rule[4])) for ticket in nearby_tickets]):
            can_be.append(i)
    print(len(can_be))
    print(can_be)
    can_be_l.append(can_be)

# Solve through inspection ... :/
