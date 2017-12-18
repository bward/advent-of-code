from collections import defaultdict

class Player:
    _registers = defaultdict(int)
    _instructions = []
    _current_instruction = 0
    _last_sound = 0
    _done = False
    _listener = None
    _send = []
    done = False
    send_count = 0

    def __init__(self, instructions, program_id):
        self._instructions = instructions
        self._registers['p'] = program_id

    def _val(self, x):
        try:
            return int(x)
        except ValueError:
            return self._registers[x]

    def add_listener(self, listener):
        self._listener = listener

    def receive(self):
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
            try:
                self._registers[instruction[1]] = self._listener.receive()
                self.done = False
            except IndexError:
                self.done = True
                return
        elif instruction[0] == 'jgz':
            if self._registers[instruction[1]]:
                self._current_instruction += self._val(instruction[2])
                return
        self._current_instruction += 1
    
    def run(self):
        while self._current_instruction < len(self._instructions) and not self._done:
            self.step()
        return self._last_sound


with open('./data/18') as puzzle_input:
    instructions = [line.rsplit() for line in puzzle_input]
    player_1 = Player(instructions, 0)
    player_2 = Player(instructions, 1)
    player_1.add_listener(player_2)
    player_2.add_listener(player_1)
    while not (player_1.done and player_2.done):
        print('stepping')
        player_1.step()
        player_2.step()
    print(player_2.send_count)