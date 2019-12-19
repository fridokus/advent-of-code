#!/usr/bin/python3
import intcode

class Camera(object):
    def __init__(self, prog):
        self.computer = intcode.IntCode(prog)
        self.space = set()
        self.scaffold = set()
        self.vaccuum_robot = tuple()

    def run_until_done(self):
        while not self.computer.done:
            self.computer.execute()

    def parse_outputs(self):
        loc = (0, 0)
        for output in self.computer.out:
            if output == 10:
                loc = (0, loc[1] + 1)
                continue
            elif output == 46:
                self.space.add(loc)
            elif output == 35:
                self.scaffold.add(loc)
            elif output == 60:
                self.vaccuum_robot = loc
            elif output == 62:
                self.vaccuum_robot = loc
            elif output == 94:
                self.vaccuum_robot = loc
            elif output == 118:
                self.vaccuum_robot = loc
            loc = (loc[0] + 1, loc[1])

    def check_surrounding(self, point):
        ret = (point[0] - 1, point[1]) in self.scaffold and \
              (point[0] + 1, point[1]) in self.scaffold and \
              (point[0], point[1] - 1) in self.scaffold and \
              (point[0], point[1] + 1) in self.scaffold
        return ret

    def sum_aligntment_parameters(self):
        alignment_sum = 0
        for point in self.scaffold:
            if self.check_surrounding(point):
                alignment_sum += point[0] * point[1]
        print(alignment_sum)

def part_1():
    prog = intcode.parse_prog('17.in')
    camera = Camera(prog)
    camera.run_until_done()
    camera.parse_outputs()
    camera.sum_aligntment_parameters()

part_1()

