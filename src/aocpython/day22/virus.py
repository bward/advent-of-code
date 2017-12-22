from collections import defaultdict
from operator import add

def sum(first, second):
    return tuple(map(add, first, second))

def create_grid(start):
    grid = defaultdict(lambda: '.')
    for i, line in enumerate(start):
        for j, char in enumerate(line.rstrip()):
            grid[(j-12, 12-i)] = char
    return(grid)

def count_infections(grid, moves, bursts):
    position = (0, 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = (0, 1)
    count = 0

    for _ in range(bursts):
        index = [m[0] for m in moves].index(grid[position])
        direction = directions[(directions.index(direction) + moves[index][1]) % 4]
        new_value = moves[(index + 1) % len(moves)][0]
        grid[position] = new_value

        if new_value == '#': count += 1
        position = sum(position, direction)

    return count

with open('./data/22') as puzzle_input:
    data = puzzle_input.readlines()
    part1_moves = [('.', -1), ('#', 1)]
    part2_moves = [('.', -1), ('W', 0), ('#', 1), ('F', 2)]

    print(count_infections(create_grid(data), part1_moves, 10000))
    print(count_infections(create_grid(data), part2_moves, 10000000))
    
