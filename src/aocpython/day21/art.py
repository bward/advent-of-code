from math import sqrt

picture = '.#./..#/###'

class Picture():
    def __init__(self, start, rules):
        self.picture = start.split('/')
        self._rules = rules

    def enhance(self):
        parts = self._parts()
        enhanced_parts = [self._rules.match(part) for part in parts]
        self._assemble(enhanced_parts)

    def count_pixels(self):
        return ''.join(self.picture).count('#')

    def _parts(self):
        size = 2 if len(self.picture) % 2 == 0 else 3
        return [tuple([self.picture[k][j:j+size] for k in range(i, i+size)]) for i in range(0, len(self.picture), size) for j in range(0, len(self.picture), size)]

    def _assemble(self, parts):
        size = int(sqrt(len(parts)))
        self.picture = [row for chunk in [[''.join(row) for row in zip(*parts[j:j+size])] for j in range(0, len(parts), size)] for row in chunk]


class Rules():
    def __init__(self, raw_rules):
        lines = [line.rsplit() for line in raw_rules]
        self._rules = {}
        for line in lines:
            self._rules[tuple(line[0].split('/'))] = tuple(line[2].split('/'))

    def match(self, block):
        matches = [block, self._flip(block)]
        for i in range(3):
            matches += [self._rotate(b) for b in matches[-2:]]
        for m in matches:
            if m in self._rules.keys(): return self._rules[m]

    def _rotate(self, block):
        return tuple([''.join(line) for line in zip(*block[::-1])])

    def _flip(self, block):
        return tuple([line[::-1] for line in block])

with open('./data/21') as puzzle_input:
    rules = Rules(puzzle_input)
    picture = Picture(picture, rules)

    [picture.enhance() for _ in range(5)]
    print(picture.count_pixels())
    [picture.enhance() for _ in range(13)]
    print(picture.count_pixels())
