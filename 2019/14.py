#!/usr/bin/python3
import math

class Formula():
    def __init__(self, formula):
        self.formula = formula.strip('\n')

    def parse_formula(self):
        arrow_split = self.formula.split(' => ')
        reactant_list = arrow_split[0].split(', ')
        self.reactants = {}
        for reactant in reactant_list:
            self.reactants[reactant.split(' ')[1]] = int(reactant.split(' ')[0])
        self.result_quantity = int(arrow_split[1].split(' ')[0])
        self.result_name = arrow_split[1].split(' ')[1]

    def __repr__(self):
        ret = 'Result: ' + str(self.result_quantity) + ' ' + self.result_name
        ret += ', Reactants: ' + str(self.reactants)
        return ret

def add_to_dict(d, key, value):
    if key in d:
        d[key] += value
    else:
        d[key] = value

def reduce_by_spare(wanted_dict, spare_dict):
    for spare in spare_dict:
        if spare in wanted_dict:
            if spare_dict[spare] > wanted_dict[spare]:
                spare_dict[spare] -= wanted_dict[spare]
                wanted_dict[spare] = 0
            elif spare_dict[spare] < wanted_dict[spare]:
                wanted_dict[spare] -= spare_dict[spare]
                spare_dict[spare] = 0
            else:
                wanted_dict[spare] = 0
                spare_dict[spare] = 0

f = open('14.in', 'r')
lines = f.readlines()
formulas = []
for line in lines:
    formulas.append(Formula(line))
    formulas[-1].parse_formula()

wanted_dict = {'FUEL': 2371699} # brute forced this number manually in 2 mins XD fastest way but way to hacky really...
done = False
spare_dict = {}
while not done:
    for formula in formulas:
        reduce_by_spare(wanted_dict, spare_dict)
        if formula.result_name in wanted_dict:
            quantity_wanted = wanted_dict[formula.result_name]
            quantity_given = formula.result_quantity
            times_this_formula = int(math.ceil(quantity_wanted / quantity_given))
            quantity_spare = quantity_given * times_this_formula - quantity_wanted
            for reactant in formula.reactants:
                add_to_dict(wanted_dict, reactant, formula.reactants[reactant] * times_this_formula)
            if quantity_spare:
                add_to_dict(spare_dict, formula.result_name, quantity_spare)
            del wanted_dict[formula.result_name]
            print(wanted_dict)

    done = True
    for wanted in wanted_dict:
        if wanted != 'ORE':
            done = False

print(wanted_dict)
