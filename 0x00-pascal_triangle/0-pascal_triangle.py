#!/usr/bin/python3
def pascal_triangle(n):

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    if n > 2:
        result = [[1], [1, 1]]
        for i in range(1, n-1):
            w = result[i]
            new = [w[0]]
            new.extend([w[e] + w[e+1] for e in range(i)])
            new.append(w[-1])
            result.append(new)
        return result
