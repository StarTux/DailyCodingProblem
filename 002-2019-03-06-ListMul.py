#!/usr/bin/python3

# Given an array of integers, return a new array such that each
# element at index i of the new array is the product of all the
# numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected
# output would be [120, 60, 40, 30, 24]. If our input was [3, 2,
# 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def solution1(list):
    val = 1
    for num in list: val *= num
    result = []
    for num in list: result.append(int(val / num))
    return result

# No division.
# Time: O(N^2)
def solution2(list):
    result = []
    for i in range(len(list)):
        prod = 1
        for j, num in enumerate(list):
            if i != j: prod *= num
        result.append(prod)
    return result

def solution3(input):
    result = []
    val = 1
    for num in input:
        for i in range(len(result)):
            result[i] *= num
        result += [val]
        val *= num
    return result

# Successively multiply up the list members, once forward, once
# backward.  The product of every two matching list entries is the
# result. No division.
#
# Time: O(N)
# Space: O(N)
def solution4(input):
    size = len(input)
    left = [1] * size # forward, result
    right = [1] * size # backward
    for i in range(1, size):
        left[i] = input[i - 1] * left[i - 1]
        j = size - i - 1
        right[j] = input[j + 1] * right[j + 1]
    for i in range(size):
        left[i] *= right[i]
    return left
        

def test(input, solution):
    output = solution4(input)
    print(f"{input} => {output} ({output == solution})")

test([1,2,3,4,5], [120, 60, 40, 30, 24])
test([3,2,1], [2, 3, 6])
test([100], [1])
