from collections import defaultdict

class Turing():
    def __init__(self):
        self._states = {}
        self._states['a'] = [(1, 1, 'b'), (0, -1, 'b')]
        self._states['b'] = [(0, 1, 'c'), (1, -1, 'b')]
        self._states['c'] = [(1, 1, 'd'), (0, -1, 'a')]
        self._states['d'] = [(1, -1, 'e'), (1, -1, 'f')]
        self._states['e'] = [(1, -1, 'a'), (0, -1, 'd')]
        self._states['f'] = [(1, 1, 'a'), (1, -1, 'e')]

        self._tape = defaultdict(int)
        self._pos = 0
        self._state = 'a'
    
    def step(self):
        state = self._states[self._state]
        instructions = state[0] if self._tape[self._pos] == 0 else state[1]
        self._tape[self._pos] = instructions[0]
        self._pos += instructions[1]
        self._state = instructions[2]

    def checksum(self):
        return sum(self._tape.values())

machine = Turing()
for _ in range(12586542):
    machine.step()
print(machine.checksum())