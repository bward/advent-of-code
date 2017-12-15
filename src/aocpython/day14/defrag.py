from ..day10.knot_hash import knot_hash
from ..day12.pipes import count_components

puzzle_input = "uugsqrei"

rows = [knot_hash('{}-{}'.format(puzzle_input, i)) for i in range(128)]
binary_rows = ['{0:02b}'.format(int(row, 16)).zfill(128) for row in rows]

def count_ones(grid):
    return sum(sum(1 for c in row if c is '1') for row in binary_rows)

def find_adjacencies(grid):
    adjacencies = {}
    for i in range(128):
        for j in range(128):
            connected = [128*x+y for x,y in [(i, min(j+1, 127)), (min(i+1,127), j), (i, max(j-1,0)), (max(i-1,0), j)] if binary_rows[x][y]=="1"]
            if(binary_rows[i][j] == "1"):   
                adjacencies[i*128+j] = connected
    return adjacencies

print(count_ones(binary_rows), count_components(find_adjacencies(binary_rows)))