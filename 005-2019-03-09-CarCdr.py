#!/usr/bin/python3

# Problem #5 [Medium]

# cons(a, b) constructs a pair, and car(pair) and cdr(pair)
# returns the first and last element of that pair. For example,
# car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

def car(pair):
    return pair(lambda a, b : a)

def cdr(pair):
    return pair(lambda a, b : b)

print(car(cons(1, 2)))
print(cdr(cons(1, 2)))

list = cons(1, cons(2, cons(3, cons(4, cons(5, None)))))

def printList(ls):
    if ls is None:
        return;
    print(car(ls))
    printList(cdr(ls))

print("print list")
printList(list)
