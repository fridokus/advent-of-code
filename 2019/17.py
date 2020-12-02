#!/usr/bin/python3
import intcode
import matplotlib.pyplot as plt

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
            elif output == 60: # left
                self.vaccuum_robot = loc
            elif output == 62: # right
                self.vaccuum_robot = loc
            elif output == 94: # up
                self.vaccuum_robot = loc
            elif output == 118: # down
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

    def run_2(self):
        self.computer.inputs = self.main_routine + self.func_a + self.func_b + self.func_c + self.live_feed
        self.run_until_done()
        print(self.computer.out[-1])
        if 88 in self.computer.out:
            print('ded')

def part_1():
    prog = intcode.parse_prog('17.in')
    camera = Camera(prog)
    camera.run_until_done()
    camera.parse_outputs()
    camera.sum_aligntment_parameters()
    list_scaffold = list(camera.scaffold)
    plt.scatter([list_scaffold[i][0] for i in range(len(list_scaffold))], [list_scaffold[i][1] for i in range(len(list_scaffold))])
    plt.savefig('17_camera_out.pdf')
    print(camera.vaccuum_robot)

def part_2():
    prog = intcode.parse_prog('17.in')
    prog[0] = 2
    camera = Camera(prog)
    # From inspection.... x)
    camera.func_a = [76, 44, 49, 48, 44, 82, 44, 56, 44, 76, 44, 54, 44, 82, 44, 54, 10]
    camera.func_b = [76, 44, 56, 44, 76, 44, 56, 44, 82, 44, 56, 10]
    camera.func_c = [82, 44, 56, 44, 76, 44, 54, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
    camera.main_routine = [65, 44, 66, 44, 65, 44, 67, 44, 65, 44, 66, 44, 67, 44, 66, 44, 67, 44, 66, 10]
    camera.live_feed = [110, 10]
    camera.run_2()

part_1()
part_2()
