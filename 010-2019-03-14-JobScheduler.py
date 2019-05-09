#!/usr/bin/python3

# Problem #10 [Medium]
#
# Implement a job scheduler which takes in a function f and an
# integer n, and calls f after n milliseconds.

import time

jobQueue = []

class Job:
    def __init__(self, fun, time):
        self.fun = fun
        self.time = time

def schedule(fun, millis):
    now = time.time()
    job = Job(fun, now + millis / 1000.0)
    jobQueue.append(job)
    jobQueue.sort(key = lambda job : job.time, reverse = True)

for i in reversed(range(4)):
    def test(num):
        print(f"scheduling {num} in {num} seconds.")
        schedule(lambda : print(num), num * 1000)
    test(i)

while len(jobQueue) > 0:
    now = time.time()
    job = jobQueue[len(jobQueue) - 1]
    if job.time < now:
        job.fun()
        jobQueue.pop()
    else:
        time.sleep(job.time - now)
