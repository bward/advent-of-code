from collections import Counter
from typing import List

def part1() -> List[str]:
    with open('./data/04') as puzzle_input:
        passphrases = (line.rstrip().split(' ') for line in puzzle_input)
        return [p for p in passphrases if len(set(p)) == len(p)]

def part2() -> List[str]:
    return [p for p in part1() if len(set(frozenset(Counter(word).items()) for word in p)) == len(p)]


print(len(part1()), len(part2()))
