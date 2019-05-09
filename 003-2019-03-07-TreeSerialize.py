#!/usr/bin/python3

# Problem #3 [Medium]

# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
# 
# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

DELIM = '|'

def serialize(node):
    result = node.val + DELIM
    if node.left is not None:
        result += serialize(node.left)
    result += DELIM
    if node.right is not None:
        result += serialize(node.right)
    return result

def deserialize(str):
    toks = str.split(DELIM)
    return deserializeHelper(toks, 0)

def deserializeHelper(toks, index):
    val = toks[index]
    if len(val) == 0: return None
    left = deserializeHelper(toks, index + 1)
    right = deserializeHelper(toks, index + 2)
    return Node(val, left, right)

# The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print(serialize(node))
