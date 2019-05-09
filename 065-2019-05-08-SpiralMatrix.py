#!/usr/bin/python3

# Daily Coding Problem #65 [Easy]

# This problem was asked by Amazon.
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# For example, given the following matrix:

example1 = [[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

def solution1(matrix):
    x, y = 0, 0
    dx, dy = 1, 0
    size = sum(map(lambda x : len(x), matrix))
    for i in range(size):
        print(matrix[y][x])
        matrix[y][x] = None
        nx = x + dx
        ny = y + dy
        if ny < 0 or ny == len(matrix) or nx < 0 or nx == len(matrix[y]) or matrix[ny][nx] is None:
            tmp = dy
            dy = dx
            dx = -tmp
        x += dx
        y += dy

solution1(example1)
