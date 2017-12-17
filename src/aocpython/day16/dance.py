def spin(programs, amount):
    programs =  programs[-amount:] + programs[:-amount]
    return(programs)

def exchange(programs, a, b):
    programs[a], programs[b] = programs[b], programs[a]
    return programs

def partner(programs, a, b):
    a_index = programs.index(a)
    b_index = programs.index(b)
    programs[a_index], programs[b_index] = programs[b_index], programs[a_index] 
    return programs

'''with open('./data/16') as puzzle_input:
    dance = puzzle_input.read().split(',')
    programs = list('abcdefghijklmnop')
    seen=[]
    for _ in range(1000000000):
        for move in dance:
            if move[0] == 's':
                programs = spin(programs, int(move[1:]))
            elif move[0] == 'x':
                programs = exchange(programs, int(move[1:].split('/')[0]), int(move[1:].split('/')[1]))
            elif move[0] == 'p':
                programs = partner(programs, move[1], move[3])
        if ''.join(programs) in seen:
            print(seen[999999999 % len(seen)])
            print(seen, len(seen))
            break
        seen.append(''.join(programs))'''


permutation = list('aodejhkblmpcgnifa')
programs = list('abcdefghijklmnop')
seen=[]
def permute(programs):
    new_programs = []
    for c in programs:
        new_programs.append(permutation[(permutation.index(c)+1)])
    return new_programs

for _ in range(1000000000):
    programs = permute(programs)
    if programs in seen:
        print(''.join(seen[1000000000 % len(seen)]))
        print(len(seen), seen)
        break
    seen.append(programs)

