#!/usr/bin/python3

# Given an array of integers, find the first missing positive
# integer in linear time and constant space. In other words, find
# the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input
# [1, 2, 0] should give 3.
# 
# You can modify the input array in-place.

def solution1(ls):
    ls.sort()
    a = 1
    for i in ls:
        if (i < a): continue
        if a == i: a += 1
    return a

def solution2(ls):
    done = set(ls)
    result = 1
    while result in done: result += 1
    return result

def solution3(ls):
    cap = len(ls)
    i = 0
    # Move non-positives to end of list.
    while i < cap:
        num = ls[i]
        if num <= 0:
            cap -= 1
            ls[i] = ls[cap]
            ls[cap] = num
        i += 1
    # Mark indexes of numbers - 1 negative
    for i in range(cap):
        num = abs(ls[i]) - 1
        if num < cap and num >= 0 and ls[num] > 0:
            ls[num] = -ls[num]
    # Return first non-negative index + 1
    for i in range(cap):
        if ls[i] > 0:
            return i + 1
    # Default: Return size of list + 1
    return cap + 1

def test(input):
    print(f"{input} => {solution3(input)}")
test([3, 4, -1, 1])
test([1, 2, 0])
test([1, 2, 3, 4, 5, 6])
test([2, 3, 4, 5, 6])
