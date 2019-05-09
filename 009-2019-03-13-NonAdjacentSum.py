#!/usr/bin/python3

# Problem #9 [Hard]
#
# Given a list of integers, write a function that returns the
# largest sum of non-adjacent numbers. Numbers can be 0 or
# negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2,
# 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

def solution1(ls):
    if len(ls) == 0: return 0
    elif len(ls) == 1: return ls[0]
    elif len(ls) == 2: return max(ls)
    result = 0
    for i, pv in enumerate(ls):
        sm = pv + solution1(ls[:max(0, i-2)] + [0] + ls[i+2:])
        if sm > result: result = sm
    return result

def solution2(ls):
    return solution2Helper(0, ls)

def solution2Helper(idx, ls):
    if idx >= len(ls): return 0
    if ls[idx] <= 0: return solution2Helper(idx + 1, ls)
    sum1 = ls[idx] + solution2Helper(idx + 2, ls)
    sum2 = solution2Helper(idx + 1, ls)
    return max(sum1, sum2)

# GOLD STAR BONUS
def solution3(ls):
    result = 0
    for idx in range(len(ls)):
        num = max(0, ls[idx])
        oldVal = ls[idx - 1] if idx >= 1 else 0
        newVal = num
        if idx >= 2: newVal += max(0, ls[idx - 2])
        ls[idx] = max(oldVal, newVal)
        if newVal > result: result = newVal
    return result

def test(input):
    print(str(input) + " => " + str(solution3(input)))

test([2, 4, 6, 2, 5])
test([5, 1, 1, 5])
test([2, 11, 6, 2, 12])
test([2, -11, 6, 2, 0])
