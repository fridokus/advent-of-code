#!/usr/bin/python3

with open('8.in') as f:
    code = f.read().splitlines()

class Gameboy():
    def __init__(self):
        self.acc = 0
        self.ptr = 0
        self.executed_instructions = set()

    def execute(self, instruction):
        op = instruction[:3]
        val = int(instruction[4:])

        if op == 'nop':
            self.ptr += 1

        elif op == 'acc':
            self.acc += val
            self.ptr += 1

        elif op == 'jmp':
            self.ptr += val

    def run_until_done(self, code):
        while True:
            if self.ptr in self.executed_instructions:
                return 1

            if self.ptr == len(code):
                return 0

            self.executed_instructions.add(self.ptr)
            self.execute(code[self.ptr])

gameboy = Gameboy()

gameboy.run_until_done(code)

print(gameboy.acc)

# b

attempt_change = gameboy.executed_instructions

for change_code_nr in attempt_change:
    modified_code = [i for i in code]
    if modified_code[change_code_nr][:3] == 'nop':
        modified_code[change_code_nr] = 'jmp' + code[change_code_nr][3:]
    elif modified_code[change_code_nr][:3] == 'jmp':
        modified_code[change_code_nr] = 'nop' + code[change_code_nr][3:]
    else:
        continue
    gameboy = Gameboy()
    if not gameboy.run_until_done(modified_code):
        break

print(gameboy.acc)
