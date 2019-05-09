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

# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

example2 = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't']]

# First solution has a 2 directional variables which we rotate as
# needed.  We also have to keep track of already visited cells.
def solution1(matrix):
    m = len(matrix[0])
    n = len(matrix)
    x, y = 0, 0
    dx, dy = 1, 0
    size = sum(map(lambda x : len(x), matrix))
    done = set()
    for i in range(size):
        yield matrix[y][x]
        done.add((x, y))
        nx = x + dx
        ny = y + dy
        if ny < 0 or ny == n or nx < 0 or nx == m or (nx, ny) in done:
            # Rotate
            dx, dy = -dy, dx
        x += dx
        y += dy

# Solution 2 only keeps track of the outer bounds.  We iterate over
# the outer rows and columns for a total of 4 times, then treat the
# remaining cells as an inner matrix.
def solution2(matrix):
    m = len(matrix[0])
    n = len(matrix)
    ax = 0
    ay = 0
    bx = m - 1
    by = n - 1
    while ax <= bx and ay <= by:
        # top
        for x in range(ax, bx + 1):
            yield(matrix[ay][x])
        # right
        for y in range(ay + 1, by + 1):
            yield(matrix[y][bx])
        # bottom
        if ay != by:
            for x in range(bx - 1, ax - 1, -1):
                yield(matrix[by][x])
        # left
        if ax != bx:
            for y in range(by - 1, ay, -1):
                yield(matrix[y][ax])
        ax += 1
        ay += 1
        bx -= 1
        by -= 1

success = 0
failure = 0
count = 1
def test(inp, solution):
    global count
    count += 1
    print("## Input " + str(count))
    for i in inp: print(" " + str(i))
    sol = solution2(inp)
    print("## Output " + str(count))
    if False:
        for i in sol: print(" " + str(i))
    else:
        sol1 = list(solution1(inp))
        sol2 = list(solution2(inp))
        print(" S" + str(solution))
        print(" 1 " + str(sol1))
        print(" 2 " + str(sol2))
        if sol1 == sol2 == solution:
            global success
            success += 1
            print(" SUCCESS")
        else:
            global failure
            failure += 1
            print(" FAILURE")

test(example1, [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12])
print()
test(example2, ['a', 'b', 'c', 'd', 'e', 'j', 'o', 't', 's', 'r', 'q', 'p', 'k', 'f', 'g', 'h', 'i', 'n', 'm', 'l'])
print()
test([[1,2,3]], [1,2,3])
print()
test([[1],
      [2],
      [3]], [1,2,3])
print()
test([[1,2],
      [3,4]], [1,2,4,3])
print()
test([[1,2],
      [3,4],
      [5,6]], [1,2,4,6,5,3])
print("success=" + str(success) + " failure=" + str(failure))
