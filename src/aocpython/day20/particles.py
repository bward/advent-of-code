with open('./data/20') as puzzle_input:
    particles = [[[int(x) for x in vector[3:-1].split(',')] for vector in line.strip().rsplit(', ')] for line in puzzle_input]
    accelerations = [[p, sum([abs(x)**2 for x in p[2]])] for p in particles]
    accelerations = sorted(accelerations, key=lambda p: p[1])
    print(particles.index(accelerations[0][0]))