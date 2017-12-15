puzzle_input = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
seen = set()

while tuple(puzzle_input) not in seen:
    seen.add(tuple(puzzle_input))
    bank_index = puzzle_input.index(max(puzzle_input))
    value = puzzle_input[bank_index]
    puzzle_input[bank_index] = 0
    for i in range(value):
        puzzle_input[(bank_index + i + 1) % len(puzzle_input)] += 1
    if puzzle_input == [1, 0, 14, 14, 12, 12, 10, 10, 8, 8, 6, 6, 4, 3, 2, 1]:
        print(len(seen))

print(len(seen))
print(puzzle_input)