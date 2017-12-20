from operator import add
from collections import Counter

class Particle():
    def __init__(self, data):
        self.pos, self.vel, self.acc = data

    def tick(self):
        self.vel = self._add(self.vel, self.acc)
        self.pos = self._add(self.pos, self.vel)

    def _add(self, a, b):
        return tuple(map(add, a, b))



with open('./data/20') as puzzle_input:
    particles = [[tuple([int(x) for x in vector[3:-1].split(',')]) for vector in line.strip().rsplit(', ')] for line in puzzle_input]

    accelerations = [[p, sum([abs(x)**2 for x in p[2]])] for p in particles]
    accelerations = sorted(accelerations, key=lambda p: p[1])
    print(particles.index(accelerations[0][0]))

    particles = [Particle(p) for p in particles]

    for _ in range(1000):
        [p.tick() for p in particles]
        positions = Counter([p.pos for p in particles])
        particles = [p for p in particles if positions[p.pos] == 1]

    print(len(particles))

