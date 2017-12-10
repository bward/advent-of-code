programs = []
with open('./input') as puzzle_input:
    lines = [line.rsplit() for line in puzzle_input]
    programs = [(line[0], int(line[1][1:-1]), [p.replace(',', '') for p in line[3:]]) for line in lines]

def part1():
    current = programs[0][0]
    while True:
        print('current:', current)
        under = [p for p in programs if len(p) > 2 and current in p[2]]
        print(under)
        if len(under) == 0:
            print(current)
            break
        current = under[0][0]
        print(current)

def tree_weight(base):
    base_node = [p for p in programs if p[0]==base][0]
    nodes = [p[2] for p in programs if p[0] == base_node[0] and len(p) > 2]
    if nodes:
        return base_node[1] + sum([tree_weight(b) for b in nodes[0]])
    else:
        print(base_node)
        return base_node[1]

base = 'tlskukk'
base_nodes = [p[2] for p in programs if p[0] == base][0]
print(base_nodes)
print([tree_weight(node) for node in base_nodes])
