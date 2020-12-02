#!/usr/bin/python3

import intcode 
import matplotlib.pyplot as plt

steps = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0),
        }

class PaintingRobot(object):
    def __init__(self, prog):
        self.direction = 0
        self.outputs = [0, 0]
        self.brain = intcode.IntCode(prog, [1 for i in range(100)])
        self.white = set()
        self.black = set()
        self.loc = (0, 0)

    def paint_loop(self):
        while not self.brain.done:
            self.paint()

    def paint(self):
        for i in range(2): # want 2 outputs
            self.brain.execute()
            self.outputs[i] = self.brain.out[-1]

        if self.brain.done:
            return

        if self.outputs[0] == 0:
            if self.loc in self.white:
                self.white.remove(self.loc)
            self.black.add(self.loc)
        elif self.outputs[0] == 1:
            if self.loc in self.black:
                self.black.remove(self.loc)
            self.white.add(self.loc)

        if self.outputs[1] == 0:
            self.direction = (self.direction - 1) % 4
        elif self.outputs[1] == 1:
            self.direction = (self.direction + 1) % 4
        self.loc = tuple((self.loc[i] + steps[self.direction][i] for i in range(2)))

        if self.loc in self.white:
            self.brain.inputs = [1 for i in range(100)]
        else:
            self.brain.inputs = [0 for i in range(100)]


    @property
    def panels_painted(self):
        painted = len(self.white) + len(self.black)
        return painted


prog = intcode.parse_prog('11.in')
robot = PaintingRobot(prog)
robot.paint_loop()
print(robot.panels_painted)


# b

list_white = list(robot.white)
plt.scatter([list_white[i][0] for i in range(len(list_white))], [list_white[i][1] for i in range(len(list_white))])
plt.savefig('11b_out.pdf')




