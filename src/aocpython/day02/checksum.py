from itertools import permutations

def part1():
    return sum(max(row) - min(row) for row in data)

def part2():
    return sum([[x//y for x, y in permutations(row, 2) if x % y == 0][0] for row in data])

with open('./data/02') as puzzle_input:
    data = [[int(d) for d in row.split('\t')] for row in puzzle_input]
    print(part1(), part2())
