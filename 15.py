#!/usr/bin/python3
import intcode
import random

directions = {
        1: (0, 1),
        2: (0, -1),
        3: (-1, 0),
        4: (1, 0)
        }

class RepairDroid(object):
    def __init__(self, prog):
        self.brain = intcode.IntCode(prog)
        self.done = False
        self.loc = (0, 0)
        self.traversed = set()
        self.wall = set()
        self.shortest_path_traversed = set()

    def repair_loop(self):
        iteration = 0
        oxygen_iteration = 0
        while not self.done:
            iteration += 1
            direction_index = self.get_input()
            self.brain.inputs = [direction_index]
            self.brain.execute()
            status = self.brain.out[-1]
            potential_loc = tuple((self.loc[i] + directions[direction_index][i] for i in range(2)))
            if status:
                self.loc = potential_loc
                if status == 2:
                    self.oxygen_tank = self.loc
                    oxygen_iteration = iteration
                else:
                    self.traversed.add(self.loc)
            else:
                self.wall.add(potential_loc)
            if oxygen_iteration and iteration == 2 * oxygen_iteration: # discover everything..
                self.done = True
                print('oxygen reached')
            if not iteration % 10000:
                print('10000')

    def get_input(self):
        return random.randint(1,4)

    def find_shortest_path(self):
        iteration = 0
        self.oxygen_tank_reached = False
        rand = set((0, 0))
        while not self.oxygen_tank_reached:
            iteration += 1
            rand = self.expand_rand(rand)
        print(iteration)

    def expand_rand(self, rand):
        new_rand = set()
        for point in rand:
            if point in self.traversed and not point in self.shortest_path_traversed:
                new_rand.add(point)
                self.shortest_path_traversed.add(point)
            elif point == self.oxygen_tank:
                self.oxygen_tank_reached = True
        return new_rand




prog = intcode.parse_prog('15.in')
repair_droid = RepairDroid(prog)
repair_droid.repair_loop()
repair_droid.find_shortest_path()


