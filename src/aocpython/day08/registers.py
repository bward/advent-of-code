from collections import defaultdict

with open('./data/08') as puzzle_input:
    instructions = [line.rsplit() for line in puzzle_input]

registers = defaultdict(int)
max_value = 0

for instruction in instructions:
    if instruction[5] == "==":
        if registers[instruction[4]] != int(instruction[6]): continue
    elif instruction[5] == "!=":
        if registers[instruction[4]] == int(instruction[6]): continue
    elif instruction[5] == "<":
        if registers[instruction[4]] >= int(instruction[6]): continue
    elif instruction[5] == ">":
        if registers[instruction[4]] <= int(instruction[6]): continue
    elif instruction[5] == "<=":
        if registers[instruction[4]] > int(instruction[6]): continue
    elif instruction[5] == ">=":
        if registers[instruction[4]] < int(instruction[6]): continue

    if instruction[1] == "inc":
        registers[instruction[0]] += int(instruction[2])
    else:
        registers[instruction[0]] -= int(instruction[2])

    max_value = max(max_value, max(registers.values()))


print(max(registers.values()), max_value)