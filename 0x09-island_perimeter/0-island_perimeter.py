#!/usr/bin/python3
"""calculates the perimeter in the
Island in a grid"""


def island_perimeter(grid):
    """this calculates the perimeter."""
    length = len(grid)
    length2 = len(grid[0])
    per = 0
    side = 0
    for i in range(length):
        for a in range(length2):
            if grid[i][a] == 1:
                per += 1
                if a > 0:
                    if grid[i][a - 1] == 1:
                        side += 1
                if i > 0:
                    if grid[i - 1][a] == 1:
                        side += 1

    return per * 4 - side * 2
