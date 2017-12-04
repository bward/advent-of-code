from math import floor, ceil, sqrt
from itertools import count
from typing import Set

puzzle_input = 361527

def part1() -> int:
    bound = ceil(sqrt(puzzle_input))
    midpoint = (bound**2+(bound-1)**2+1)//2
    distance = abs(bound//2 - abs(puzzle_input - midpoint))
    return distance + bound//2

def get_neighbours(i) -> Set[int]:
    bound = ceil(sqrt(i))
    midpoint = (bound**2+(bound-1)**2+1)//2
    distance = i - midpoint
    previous_midpoint = ((bound-2)**2+((bound-1)-2)**2+1)//2

    if i < midpoint:
        previous = [(bound-1)**2] + list(range((bound-3)**2+1, previous_midpoint+1))
    else:
        previous = [midpoint - 1] + list(range(previous_midpoint, (bound-2)**2+2))

    if distance < 0:
        distance = bound - 1 + distance

    indices = range(max(0, distance - 1), min(distance+2, len(previous)))
    out = set(previous[i] for i in indices)
    out.add(i-1)
    return out

def part2() -> int:
    sums = [1]
    for i in count(2):
        sums.append(sum(sums[j-1] for j in get_neighbours(i)))
        if sums[-1] > puzzle_input:
            return sums[-1]

print(part1(), part2())