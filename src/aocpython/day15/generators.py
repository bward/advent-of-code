def generator(start, factor, multiple=1):
    while True:
        start = (start * factor) % 2147483647
        if not start % multiple:
            yield start & 0xffff

def part1():
    gen_a = generator(618, 16807)
    gen_b = generator(814, 48271)
    return sum(next(gen_a) == next(gen_b) for _ in range(40000000))

def part2():
    gen_a = generator(618, 16807, 4)
    gen_b = generator(814, 48271, 8)
    return sum(next(gen_a) == next(gen_b) for _ in range(5000000))

print(part1(), part2())