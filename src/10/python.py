from functools import reduce
from operator import xor

lengths = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'

def sparse_hash(lengths, values, position, skip_size):
    for length in lengths:
        reverse = (values+values)[position:position+length][::-1]
        values = (values[:position] + reverse + values[position+length:])
        values = values[256:] + values[len(values[256:]):256]
        position += length + skip_size
        position %= 256
        skip_size += 1
    return values, position, skip_size

def dense_hash(sparse):
    return [reduce(xor, sparse[16*i:16*(i+1)]) for i in range(16)]

def knot_hash(lengths):
    lengths = [ord(c) for c in lengths] + [17, 31, 73, 47, 23]
    values = list(range(256))
    position = 0
    skip_size = 0
    for _ in range(64):
        values, position, skip_size = sparse_hash(lengths, values, position, skip_size)
    dense = dense_hash(values)
    return ''.join(['{0:02x}'.format(d) for d in dense])


sparse = sparse_hash([int(c) for c in lengths.split(',')], list(range(256)), 0, 0)
print(sparse[0][0]*sparse[0][1], knot_hash(lengths))
