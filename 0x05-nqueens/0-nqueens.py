#!/usr/bin/python3

import sys


if len(sys.argv) > 2:
    print('Usage: nqueens N')
    sys.exit(1)
elif not sys.argv[1].isdigit():
    print('N must be a number')
else:
    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
    else:
        N = int(sys.argv[1])
        for i in range(1, N - 1):
            x = 0
            y = i
            incr = y + 1
            length = 0
            result = [[x, y]]
            while length < (N - 1):
                x = x + 1
                y = y + (incr)
                if y > N:
                    y = (y % N) - 1
                result.append([x, y])
                length += 1
            print(result)
