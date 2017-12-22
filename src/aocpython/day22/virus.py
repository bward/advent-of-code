from collections import defaultdict
from operator import add

def sum(first, second):
    return tuple(map(add, first, second))

with open('./data/22') as puzzle_input:
    grid = defaultdict(lambda: '.')
    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line.rstrip()):
            grid[(j-12, 12-i)] = char

    position = (0, 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    states = ['.', 'W', '#', 'F']
    direction = (0, 1)
    count = 0

    for _ in range(10000000):
        if grid[position] == '#':
            direction = directions[(directions.index(direction) + 1) % 4]
            grid[position] = 'F'

        elif grid[position] == '.':
            direction = directions[(directions.index(direction) - 1) % 4]
            grid[position] = 'W'

        elif grid[position] == 'W':
            grid[position] = '#'
            count += 1

        elif grid[position] == 'F':
            direction = directions[(directions.index(direction) - 2) % 4]
            grid[position] = '.'
        position = sum(position, direction)

    print(count)
