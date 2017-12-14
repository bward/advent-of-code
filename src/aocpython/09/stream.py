with open('./input') as puzzle_input:
    stream = puzzle_input.read()
    garbage = False
    ignore = False
    score = 0
    nesting = 0
    cancelled = 0

    for c in stream:
        if ignore:
            ignore = False
        elif c == '>':
            garbage = False
        elif garbage and c == '!':
            ignore = True
        elif garbage:
            cancelled += 1
        elif c == '<':
            garbage = True
        elif c == '{':
            nesting += 1
        elif c == '}':
            score += nesting
            nesting -= 1

    print(score, cancelled)
