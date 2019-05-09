#!/usr/bin/python3

# Problem #16 [Easy]
#
# You run an e-commerce website and want to record the last N
# order ids in a log. Implement a data structure to accomplish
# this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is
# guaranteed to be smaller than or equal to N.
#
# You should be as efficient with time and space as possible.

class Log:
    def __init__(self, bound):
        self.bound = bound
        self.ids = [None] * bound
        self.index = -1

    def record(self, order_id):
        self.index += 1
        if self.index >= self.bound:
            self.index = 0
        self.ids[self.index] = order_id

    def get_last(self, i):
        i = self.index - i
        if i < 0:
            i += self.bound
        return self.ids[i]

log = Log(7)
import random
for i in range(5):
    log.record(int(random.random() * 100000000))
log.record(1337)
log.record(0xcafebabe)
for i in range(7):
    id = log.get_last(i)
    print(f"{i} => {id:012d}\t0x{id:x}")
