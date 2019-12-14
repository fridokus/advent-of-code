#!/usr/bin/python3

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

