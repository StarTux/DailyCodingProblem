#!/usr/bin/python3

# Problem #66 [Medium]

# This problem was asked by Square.

# Assume you have access to a function toss_biased() which returns 0
# or 1 with a probability that's not 50-50 (but also not 0-100 or
# 100-0). You do not know the bias of the coin.

# Write a function to simulate an unbiased coin toss.

import random;

bias = 0.1 + random.random() * 0.8
print("bias={0:.2f}".format(bias))
def toss_biased():
    if random.random() <= bias:
        return 1
    else:
        return 0

# The solution.
def toss_unbiased():
    while True:
        a = toss_biased()
        b = toss_biased()
        if a != b:
            yield a
        

rolls = 100000
wins = 0
losses = 0

coin = toss_unbiased()
for _ in range(rolls):
    flip = next(coin)
    if flip == 1:
        wins += 1
    else:
        losses += 1

print("rolls=" + str(rolls)
      + " wins=" + str(wins)
      + " losses=" + str(losses)
      + " (" + str(int(wins/rolls*100)) + "%)")
