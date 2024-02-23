#!/usr/bin/python3
"""interview 2d matrix module."""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    length = len(matrix)
    mixer = 0
    for i in range(length-1, 0, -2):
        for n in range(i):
            checking = mixer * (length + 1)
            x1 = int(checking / length)
            y1 = checking % length
            val = matrix[x1][y1]
            for m in range(i * 4):
                total = i * 4
                if m < total / 4:
                    checking = checking + 1
                elif m < total / 2:
                    checking = checking + length
                elif m < total - i:
                    checking = checking - 1
                elif m < total:
                    checking = checking - length
                x2 = int(checking / length)
                y2 = checking % length
                temp = matrix[x2][y2]
                matrix[x2][y2] = val
                val = temp
        mixer = mixer + 1
