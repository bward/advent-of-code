puzzle_input = []
with open('./input') as puzzle:
    puzzle_input = [int(line.rsplit()[0]) for line in puzzle]

print(puzzle_input)

def part1(jumps):
    steps = 0
    position = 0
    while -1 < position and position < len(jumps):
        instruction = jumps[position]
        if instruction > 2: jumps[position] -= 1
        else: jumps[position] += 1
        position += instruction
        steps += 1
    return steps

print(part1(puzzle_input))