from collections import Counter

def dist(x, y):
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return x+y
    else:
        return max(abs(x), abs(y))

with open('./data/11') as puzzle_input:
    steps = puzzle_input.read().split(',')
    counts = Counter(steps)

    y = counts['n'] - counts['s']
    x = counts['ne'] - counts['sw']

    se = counts['se'] - counts['nw']
    x += se
    y -= se

    print(dist(x, y))

with open('./data/11') as puzzle_input:
    x = 0
    y = 0
    max_dist = 0
    for step in puzzle_input.read().split(','):
        if step == 'ne':
            x += 1
        elif step == 'sw':
            x -= 1
        elif step == 'n':
            y += 1
        elif step == 's':
            y -= 1
        elif step == 'se':
            x += 1
            y -= 1
        elif step == 'nw':
            x -= 1
            y += 1
        max_dist = max(max_dist, dist(x,y))
    
    print(max_dist)
