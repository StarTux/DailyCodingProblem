#!/usr/bin/python3

# Daily Coding Problem: Problem #18 [Hard]

# Given an array of integers and a number k, where 1 <= k <= length of the
# array, compute the maximum values of each subarray of length k.
# 
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10,
# 7, 8, 8], since:
# 
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
#
# Do this in O(n) time and O(k) space. You can modify the input array in-place
# and you do not need to store the results. You can simply print them out as
# you compute them.

def solution1(arr, k):
    sub = arr[:k]
    subp = 0
    arrp = k
    while True:
        m = max(sub)
        s = str(sub).replace("[", "(").replace("]", ")");
        print(f"{m} = max{s}")
        if arrp >= len(arr): return
        sub[subp] = arr[arrp]
        arrp += 1
        subp = (subp + 1) % len(sub)

def test(arr, k):
    print(arr, k)
    solution1(arr, k)

test([10,5,2,7,8,7], 3)
print("")
test([1,2,3,4,5,6,7,8,9], 4)
