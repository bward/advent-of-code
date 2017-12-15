puzzle_input = []
with open('./data/05') as puzzle:
    puzzle_input = [int(line.rsplit()[0]) for line in puzzle]

def count_steps(offsets, offset_change):
    steps = 0
    offsets = list(offsets)
    position = 0
    while -1 < position and position < len(offsets):
        instruction = offsets[position]
        offsets[position] += offset_change(instruction)
        position += instruction
        steps += 1
    return steps

if __name__ == '__main__':
    print(count_steps(puzzle_input, lambda x: 1), count_steps(puzzle_input, lambda x: -1 if x > 2 else 1))