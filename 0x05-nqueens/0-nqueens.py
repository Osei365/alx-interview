#!/usr/bin/python3

import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)
if not sys.argv[1].isdigit():
    print('N must be a number')
if int(sys.argv[1]) < 4:
    print('N must be at least 4')
n = int(sys.argv[1])
def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ solve """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
