#!/usr/bin/python3

# Problem #20 [Easy]
# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

# I assume that the actual node needs to be returned, not just the
# value. BAD solution which modifies the lists. Looked up a much more
# elegant one, see solution2.
# Still a cool train of thought.
# def solution1(la, lb):
#     la = inv(la)
#     lb = inv(lb)
#     res = la
#     pre = None
#     while la[0] == lb[0]:
#         pre = la
#         la = la[1]
#         lb = lb[1]
#     pre[1] = None
#     return inv(res)

def solution2(la, lb):
    lena = lilen(la)
    lenb = lilen(lb)
    if lena > lenb:
        for _ in range(lena - lenb):
            la = la[1]
    else:
        for _ in range(lenb - lena):
            lb = lb[1]
    while la[0] != lb[0]:
        la = la[1]
        lb = lb[1]
    return la

# Find length of linked list
def lilen(ls):
    res = 1
    while ls[1] is not None:
        res += 1
        ls = ls[1]
    return res

# # invert linked list in constant space, by modifying the nodes
# def inv(el):
#     pre = None
#     e = el
#     while True:
#         tmp = e[1]
#         e[1] = pre
#         pre = e
#         if tmp is None:
#             return e
#         e = tmp

# Utility: make linked list, obviously NOT in constant space
def linked(ls):
    e = None
    for i in reversed(ls):
        e = (i, e)
    return e

def test(la, lb):
    print(la)
    print(lb)
    res = solution2(la, lb)
    print(res)

test(linked([3, 7, 8, 10]), linked([99, 1, 8, 10]))
print()
test(linked([1, 2, 3, 4, 5, 6]), linked([5, 6, 1, 4, 5, 6]))
