#!/usr/bin/python3

# Problem #8 [Easy]
#
# A unival tree (which stands for "universal value") is a tree
# where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival
# subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, value, left = None, right = None):
        if left is not None and not isinstance(left, Node):
            raise Exception('left is not Node')
        if right is not None and not isinstance(right, Node):
            raise Exception('right is not Node')
        self.value = value
        self.left = left
        self.right = right

tree =  Node(0,
            Node(1),
            Node(0,
                Node(1,
                    Node(1),
                    Node(1)),
                Node(0)))

tree2 = Node(0, right=Node(0))

def countUnival(node):
    if node is None: return 0
    result = countUnival(node.left) + countUnival(node.right)
    if countUnivalHelper(node.value, node.left) and countUnivalHelper(node.value, node.right):
        result += 1
    return result

def countUnivalHelper(value, node):
    if node is None: return True
    if node.value != value: return False
    return countUnivalHelper(value, node.left) and countUnivalHelper(value, node.right)

print("count1 = " + str(countUnival(tree)))
print("count2 = " + str(countUnival(tree2)))
