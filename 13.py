#!/usr/bin/python3

import intcode
import matplotlib.pyplot as plt
import random

class ArcadeCabinet(object):
    def __init__(self, prog, h, w):
        self.computer = intcode.IntCode(prog)
        self.screen = [[0 for i in range(w)] for i in range(h)]
        self.score = 0
        self.game_over = False
        self.init = True
        self.paddle_x = 0

    def run_until_halt(self):
        while not self.computer.done:
            for _ in range(3):
                self.computer.execute()
            self.draw_object()


    def draw_object(self):
        tile = self.computer.out[-1]
        y = self.computer.out[-2]
        x = self.computer.out[-3]
        if x == -1 and y == 0:
            self.score = tile
        else:
            self.screen[y][x] = tile
        if tile == 3:
            self.paddle_x = x
        if tile == 4:
            ball_x = x
            if ball_x < self.paddle_x:
                self.computer.inputs = [-1]
            elif ball_x > self.paddle_x:
                self.computer.inputs = [1]
            else:
                self.computer.inputs = [0]
            self.last_ball_x = ball_x

    def count_block(self):
        return sum(map(lambda x: x.count(2), self.screen))


prog = intcode.parse_prog('13.in')
prog[0] = 2
arcade_cabinet = ArcadeCabinet(prog, 108, 192)
arcade_cabinet.run_until_halt()
print(arcade_cabinet.count_block())
print(arcade_cabinet.score)
