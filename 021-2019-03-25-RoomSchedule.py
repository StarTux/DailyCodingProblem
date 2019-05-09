#!/usr/bin/python3

# Problem #21 [Easy]

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures
# (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return
# 2.

#
def solution1(inp):
    schedule = dict()
    result = 0
    for interval in inp:
        for t in range(interval[0], interval[1]):
            rooms = 0
            if t in schedule:
                rooms = schedule[t] + 1
            else :
                rooms = 1
            schedule[t] = rooms
            if rooms > result: result = rooms
    return result

def test(inp):
    rooms = solution1(inp)
    print(str(inp) + " => " + str(rooms))

test([(30, 75), (0, 50), (60, 150)])
test([(30, 75), (0, 50), (60, 150), (55, 200), (0, 210)])
test([(0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
      (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)])
test([(0,1), (0,2), (0,3),(3,5)])
