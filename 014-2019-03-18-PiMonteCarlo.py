#!/usr/bin/python3

# Problem #14 [Medium]
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal
# places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

def solution1():
    tries = 100000000
    hits = 0
    for i in range(tries):
        a = random.random()
        b = random.random()
        if a * a + b * b <= 1:
            hits += 4
    return hits / tries

def test():
    print(f"PI = {solution1()}")

from math import pi
print(f"real PI = {pi}")
test()
