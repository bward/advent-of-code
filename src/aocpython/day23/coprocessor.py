from collections import defaultdict
from math import sqrt

class Coprocessor():
    def __init__(self, instructions, debug=False):
        self._instructions = instructions
        self._registers = defaultdict(int)
        self._current_instruction = 0
        self.count = 0
        self.done = False
        if not debug:
            self._registers['a'] = 1

    def _val(self, x):
            try:
                return int(x)
            except ValueError:
                return self._registers[x]

    def step(self):
        if self._current_instruction not in list(range(len(self._instructions))):
            self.done = True
            return

        instruction = self._instructions[self._current_instruction]
        
        if instruction[0] == 'set':
            self._registers[instruction[1]] = self._val(instruction[2])
        elif instruction[0] == 'sub':
            self._registers[instruction[1]] -= self._val(instruction[2])
        elif instruction[0] == 'mul':
            self._registers[instruction[1]] *= self._val(instruction[2])
            self.count += 1
        elif instruction[0] == 'jnz':
            if self._val(instruction[1]) != 0:
                self._current_instruction += self._val(instruction[2])
                return

        self._current_instruction += 1
    
    def go(self):
        while not self.done: self.step()
        return self.count

with open('./data/23') as puzzle_input:
    instructions = [line.rsplit() for line in puzzle_input]
    coprocessor = Coprocessor(instructions, debug=True)
    print(coprocessor.go())

h = 0
b = 109900
c = 126900

for g in range(b, c + 17, 17):
    for d in range(2, int(sqrt(g)) + 1):
        if g % d == 0:
            h += 1
            break
print(h)