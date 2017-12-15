programs = []
with open('./data/07') as puzzle_input:
    lines = [line.rsplit() for line in puzzle_input]
    programs = [(line[0], int(line[1][1:-1]), [p.replace(',', '') for p in line[3:]]) for line in lines]

def tree_root(tree):
    current = tree[0][0]
    while True:
        under = [p for p in tree if len(p) > 2 and current in p[2]]
        if not under:
            return current
        current = under[0][0]

def node_weight(tree, base):
    base_node = [p for p in tree if p[0] == base][0]
    nodes = [p[2] for p in tree if p[0] == base_node[0] and len(p) > 2]
    if nodes:
        return base_node[1] + sum([node_weight(tree, b) for b in nodes[0]])
    else:
        print(base_node)
        return base_node[1]

def correct_weight(tree):
    def base_nodes(base): return [p[2] for p in programs if p[0] == base][0]
    base = tree_root(tree)
    weight_delta = 0
    while True:
        weight = node_weight(tree, base)
        nodes = base_nodes(base)
        weights = [node_weight(tree, node) for node in nodes]
        odd_weight = [w for w in weights if weights.count(w) is 1]
        if odd_weight:
            weight_delta = odd_weight[0] - [w for w in weights if weights.count(w) > 1][0]
            base = nodes[weights.index(odd_weight[0])]
        else:
            return weight - sum(weights) - weight_delta

print(tree_root(programs), correct_weight(programs))