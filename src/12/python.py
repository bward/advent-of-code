from itertools import chain

pipes = {}

with open('./input') as in_file:
    lines = [line.replace(',', '').rsplit() for line in in_file]
    for line in lines:
        pipes[int(line[0])] = [int(d) for d in line[2:]]

def grow(start):
    neighbours = list(chain.from_iterable([pipes[n] for n in start]))
    return set(start).union(neighbours)

def part1(start):    
    neighbours = grow([start])
    while len(grow(neighbours)) > len(neighbours):
        neighbours = grow(neighbours)
    return neighbours

def part2():
    groups = 0
    while len(pipes) > 0:
        start = list(pipes.keys())[0]
        group = part1(start)
        [pipes.pop(pipe) for pipe in group]
        groups += 1
    return groups

print(len(part1(0)), part2())