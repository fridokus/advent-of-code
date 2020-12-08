#!/usr/bin/python3
import re

with open('8.in') as f:
    code = re.findall('(\w+) ([+-]\d+)', f.read())

class Gameboy():
    def __init__(self):
        self.acc, self.ptr = 0, 0
        self.executed_instructions = set()

    def execute(self, instruction):
        self.executed_instructions.add(self.ptr)
        op, val = instruction

        if op == 'nop':
            self.ptr += 1

        elif op == 'acc':
            self.acc += int(val)
            self.ptr += 1

        elif op == 'jmp':
            self.ptr += int(val)

    def run_until_done(self, code):
        while self.ptr not in self.executed_instructions and self.ptr != len(code):
            self.execute(code[self.ptr])

        return self.ptr != len(code)

gameboy = Gameboy()
gameboy.run_until_done(code)
print(gameboy.acc)

# b

attempt_change = gameboy.executed_instructions

for i in attempt_change:
    if code[i][0] != 'acc':
        modified_code = code[:i] + [({'jmp': 'nop', 'nop': 'jmp'}[code[i][0]], code[i][1])] + code[i+1:]
    else:
        continue
    gameboy = Gameboy()
    if not gameboy.run_until_done(modified_code):
        break

print(gameboy.acc)
