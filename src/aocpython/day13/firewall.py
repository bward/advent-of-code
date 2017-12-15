from itertools import count

depths = {}

with open('./data/13') as in_file:
    puzzle_input = [line.rstrip().split(': ') for line in in_file]
    depths = {int(layer[0]): int(layer[1]) for layer in puzzle_input}

def scanner_position(time, depth):
    return time % (2 * (depth - 1))

def severity():
    return sum(layer * depths[layer] for layer in depths if  scanner_position(layer, depths[layer]) == 0)

def best_delay():
    return next(delay for delay in count() if not any(scanner_position(layer + delay, depths[layer]) == 0 for layer in depths))

print(severity(), best_delay())