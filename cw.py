def count_bits(n):
    k=bin(n)[2:]
    h=k.count('1')

    return h
