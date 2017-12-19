from string import ascii_uppercase

class Follower():
    def __init__(self, maze):
        self._maze = maze
        self._dir = (1, 0)
        self._pos = (0, maze[0].index('|'))
        self._letters = []
        self._steps = 0

    def go(self):
        while self._get_char() != ' ': self._step()
        return ''.join(self._letters), self._steps
    
    def _get_char(self, pos=None):
        if not pos: pos = self._pos
        return self._maze[pos[0]][pos[1]]

    def _add(self, first, second):
        return (first[0] + second[0], first[1] + second[1])

    def _step(self):
        current = self._get_char()

        if current in ascii_uppercase:
            self._letters.append(current)

        if current == '+':
            options = [(d, self._get_char(self._add(self._pos, d))) for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
            self._dir = list(filter(lambda x: x[1] != ' ' and x[1] != self._prev, options))[0][0]

        self._prev = current
        self._pos = self._add(self._pos, self._dir)
        self._steps += 1


with open('./data/19') as puzzle_input:
    maze = [[char for char in line.replace('\n', '')] for line in puzzle_input]
    follower = Follower(maze)
    print(follower.go())