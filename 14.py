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


f = open('test14.in', 'r')
lines = f.readlines()
formulas = []
for line in lines:
    formulas.append(Formula(line))
    formulas[-1].parse_formula()

wanted_dict = {'FUEL': 1}
done = False
# TODO: implement spare dict..
while not done:
    for formula in formulas:
        if formula.result_name in wanted_dict:
            quantity_wanted = wanted_dict[formula.result_name]
            quantity_given = formula.result_quantity
            times_this_formula = int(math.ceil(quantity_wanted / quantity_given))
            for reactant in formula.reactants:
                if reactant in wanted_dict:
                    wanted_dict[reactant] += formula.reactants[reactant] * times_this_formula
                else:
                    wanted_dict[reactant] = formula.reactants[reactant] * times_this_formula
            del wanted_dict[formula.result_name]
            print(wanted_dict)

    done = True
    for wanted in wanted_dict:
        if wanted != 'ORE':
            done = False

print(wanted_dict)


