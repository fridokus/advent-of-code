#!/usr/bin/python3

import intcode
import matplotlib.pyplot as plt

class ArcadeCabinet(object):
    def __init__(self, prog, h, w):
        self.computer = intcode.IntCode(prog)
        self.screen = [[0 for i in range(w)] for i in range(h)]

    def run_until_halt(self):
        while not self.computer.done:
            for _ in range(3):
                self.computer.execute()
            self.draw_object()

    def draw_object(self):
        tile = self.computer.out[-1]
        y = self.computer.out[-2]
        x = self.computer.out[-3]
        self.screen[y][x] = tile

    def count_block(self):
        return sum(map(lambda x: x.count(2), self.screen))


prog = intcode.parse_prog('13.in')
arcade_cabinet = ArcadeCabinet(prog, 108, 192)
arcade_cabinet.run_until_halt()
print(arcade_cabinet.count_block())


