step_size = 335

def part1():
    pos = 0
    buffer = [0]
    for i in range(1, 2018):
        pos = (pos + step_size) % i + 1
        buffer.insert(pos, i)
    return buffer[buffer.index(2017) + 1]

def part2():
    pos = 0
    out = 0
    for i in range(1, 50000001):
        pos = (pos + step_size) % i
        if not pos: out = i
        pos += 1
    return out

print(part1(), part2())