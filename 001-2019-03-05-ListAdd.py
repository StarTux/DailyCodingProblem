#!/usr/bin/python3

# Given a list of numbers and a number k, return whether any two
# numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since
# 10 + 7 is 17.
# 
# Bonus: Can you do this in one pass?

def solution1(ls, sum):
    done = set()
    for num in ls:
        if (sum - num) in done: return True
        done.add(num)
    return False

def test(ls, sum):
    print(f"{ls}, {sum} => {solution1(ls, sum)}")
	
test([1,2,7], 9)
test([7,1,2], 9)
test([1,2,5,7], 10)
