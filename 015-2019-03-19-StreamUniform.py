#!/usr/bin/python3

# Problem #15 [Medium]
#
# Given a stream of elements too large to store in memory, pick a
# random element from the stream with uniform probability.

import random

# Return index for testing purposes.
def solution1(input):
    result = None
    index = 1
    for i in input:
        if random.random() < 1 / index:
            result = index - 1
        index += 1
    return result

def strim(size):
    for i in range(size):
        yield random.random()

def test(secret, sample):
    stats = [0] * secret
    for i in range(sample):
        stats[solution1(strim(secret))] += 1
    percs = list(map(lambda a : a / sample * secret, stats))
    maxdev = max(abs(1 - min(percs)), abs(1 - max(percs)))
    print(f"secret={secret} sample={sample} => deviation={maxdev:.04f} {stats}")

test(2, 100)
test(2, 1000)
test(2, 10000)
test(2, 100000)
test(2, 1000000)
