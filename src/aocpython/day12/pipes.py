from itertools import chain
from typing import Dict, List, Set

def grow(pipes: Dict[int, List[int]], start: List[int]) -> Set[int]:
    neighbours = list(chain.from_iterable([pipes[n] for n in start]))
    return set(start).union(neighbours)

def component(pipes: Dict[int, List[int]], start: int) -> Set[int]:    
    neighbours = grow(pipes, [start])
    while len(grow(pipes, neighbours)) > len(neighbours):
        neighbours = grow(pipes, neighbours)
    return neighbours

def count_components(pipes: Dict[int, List[int]]) -> int:
    groups = 0
    pipes = dict(pipes)
    while pipes:
        start = list(pipes.keys())[0]
        group = component(pipes, start)
        [pipes.pop(pipe) for pipe in group]
        groups += 1
    return groups

if __name__ == '__main__':
    pipes = {}
    with open('./data/12') as in_file:
        lines = [line.replace(',', '').rsplit() for line in in_file]
        for line in lines:
            pipes[int(line[0])] = [int(d) for d in line[2:]]
    print(len(component(pipes, 0)), count_components(pipes))