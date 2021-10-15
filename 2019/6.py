#!/usr/bin/python3

class Planet():
    def __init__(self, name, parent):
        self.name = name
        if parent:
            self.depth = None
            self.parent = parent # str
        else:
            self.depth = 0
            self.parent = None

    def __repr__(self):
        return 'Planet ' + self.name

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth

    def resolve_depth(self):
        if self.parent is None:
            return
        parent_depth = planet_dict[self.parent].get_depth()
        if not parent_depth is None:
            self.depth = parent_depth + 1

def find_common_ancestor(planet1, planet2):
    ancestors1 = [planet1.parent]
    while planet_dict[ancestors1[-1]].parent:
        ancestors1.append(planet_dict[ancestors1[-1]].parent)
    ancestors2 = [planet2.parent]
    while planet_dict[ancestors2[-1]].parent:
        ancestors2.append(planet_dict[ancestors2[-1]].parent)

    ancestors1 = set(ancestors1)
    ancestors2 = set(ancestors2)
    path = ancestors1.union(ancestors2) - ancestors1.intersection(ancestors2)
    print(len(path))
    print(len(set(ancestors2).union(set(ancestors1))))

f = open('input_6.txt', 'r')
lines = f.readlines()
lines = [line.strip('\n') for line in lines]
relations = [line.split(')') for line in lines][:-1]

planet_dict = {}
com = Planet('COM', None)

planet_dict['COM'] = com

for relation in relations:
    this_planet = Planet(relation[1], relation[0])
    planet_dict[relation[1]] = this_planet

for i in range(500):
    for planet in planet_dict:
        planet_dict[planet].resolve_depth()

depths = [planet_dict[planet].get_depth() for planet in planet_dict]

# print(sum(depths))

find_common_ancestor(planet_dict['YOU'], planet_dict['SAN'])
