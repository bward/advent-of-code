from collections import defaultdict

class Player:
    def __init__(self, instructions, program_id, part1=False):
        self._instructions = instructions
        self._registers = defaultdict(int)
        self._registers['p'] = program_id
        self._send = []
        self._current_instruction = 0
        self.done = False
        self.send_count = 0
        self._part1 = part1

    def _val(self, x):
        try:
            return int(x)
        except ValueError:
            return self._registers[x]

    def add_listener(self, listener):
        self._listener = listener

    def send(self):
        return self._send.pop(0)

    def step(self):
        if self._current_instruction >= len(self._instructions):
            self.done = True
            return

        instruction = self._instructions[self._current_instruction]

        if instruction[0] == 'snd':
            self._send.append(self._val(instruction[1]))
            self.send_count += 1
        elif instruction[0] == 'set':
            self._registers[instruction[1]] = self._val(instruction[2])
        elif instruction[0] == 'add':
            self._registers[instruction[1]] += self._val(instruction[2])
        elif instruction[0] == 'mul':
            self._registers[instruction[1]] *= self._val(instruction[2])
        elif instruction[0] == 'mod':
            self._registers[instruction[1]] %= self._val(instruction[2])
        elif instruction[0] == 'rcv':
            if self._part1:
                self.done = True
                return
            try:
                self._registers[instruction[1]] = self._listener.send()
                self.done = False
            except IndexError:
                self.done = True
                return
        elif instruction[0] == 'jgz':
            if self._val(instruction[1]) > 0:
                self._current_instruction += self._val(instruction[2])
                return

        self._current_instruction += 1
    
    def part1(self):
        while self._current_instruction < len(self._instructions) and not self.done:
            self.step()
        return self._send[-1]


with open('./data/18') as puzzle_input:
    instructions = [line.rsplit() for line in puzzle_input]

    part1_player = Player(instructions, 0, True)
    print(part1_player.part1())

    player_1 = Player(instructions, 0)
    player_2 = Player(instructions, 1)
    player_1.add_listener(player_2)
    player_2.add_listener(player_1)
    while not (player_1.done and player_2.done):
        player_1.step()
        player_2.step()
    print(player_2.send_count)
