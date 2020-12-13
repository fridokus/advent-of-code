#!/usr/bin/python3

with open('12.in') as f:
    instructions = [(i[0], int(i[1:])) for i in f]

angle_map = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
class Boat:
    def __init__(self):
        self.angle = 0
        self.loc = [0, 0]

    def action(self, instr):
        if instr[0] == 'E':
            self.loc[0] += instr[1]
        elif instr[0] == 'N':
            self.loc[1] += instr[1]
        elif instr[0] == 'W':
            self.loc[0] -= instr[1]
        elif instr[0] == 'S':
            self.loc[1] -= instr[1]
        elif instr[0] == 'L':
            self.angle = (self.angle + instr[1]) % 360
        elif instr[0] == 'R':
            self.angle = (self.angle - instr[1]) % 360
        elif instr[0] == 'F':
            self.action((angle_map[self.angle], instr[1]))
        
    def navigate(self, instructions):
        for instr in instructions:
            self.action(instr)

boat = Boat()
boat.navigate(instructions)
print(abs(boat.loc[0]) + abs(boat.loc[1]))

class Boat:
    def __init__(self):
        self.angle = 0
        self.loc = [0, 0]
        self.waypoint_loc = [10, 1]

    def action(self, instr):
        if instr[0] == 'E':
            self.waypoint_loc[0] += instr[1]
        elif instr[0] == 'N':
            self.waypoint_loc[1] += instr[1]
        elif instr[0] == 'W':
            self.waypoint_loc[0] -= instr[1]
        elif instr[0] == 'S':
            self.waypoint_loc[1] -= instr[1]
        elif instr[1] == 180:
            self.waypoint_loc = [-self.waypoint_loc[0], -self.waypoint_loc[1]]
        elif (instr[0] == 'L' and instr[1] == 90) or (instr[0] == 'R' and instr[1] == 270):
            self.waypoint_loc = [-self.waypoint_loc[1], self.waypoint_loc[0]]
        elif (instr[0] == 'R' and instr[1] == 90) or (instr[0] == 'L' and instr[1] == 270):
            self.waypoint_loc = [self.waypoint_loc[1], -self.waypoint_loc[0]]
        elif instr[0] == 'F':
            self.loc = [self.loc[i] + instr[1] * self.waypoint_loc[i] for i in range(2)]
        
    def navigate(self, instructions):
        for instr in instructions:
            self.action(instr)

boat = Boat()
boat.navigate(instructions)
print(abs(boat.loc[0]) + abs(boat.loc[1]))
