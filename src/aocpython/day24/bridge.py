def extend(builds, components, total_length=None): 
    extensions = [extend_single(build, components) for build in builds]
    extensions = [i for s in extensions for i in s]
    new_total = sum([len(b) for b in extensions])
    return extensions if new_total == total_length else extend(extensions, components, total_length = new_total)

def extend_single(build, components):
    end = build[-1]
    try: free_port = end[0] if end[0] not in build[-2] else end[1]
    except: free_port = max(end)
    possible_extensions = [c for c in components if free_port in c and c not in build]
    return [build + [c] for c in possible_extensions] if possible_extensions else [build]

def strength(bridge):
    return sum([sum(c) for c in bridge])

with open('./data/24') as puzzle_input:
    components = [tuple([int(p) for p in line.rstrip().split("/")]) for line in puzzle_input]
    starts = [[c] for c in components if 0 in c]
    bridges = extend(starts, components)

    print(max([strength(s) for s in bridges]))

    max_length = max([len(b) for b in bridges])
    longest = [b for b in bridges if len(b) == max_length]
    print(max([strength(s) for s in longest]))