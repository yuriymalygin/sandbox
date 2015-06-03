#!/usr/bin/python2.7
#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

x = 0

def multiple(x):
    state = True
    limit = 20
    
    for i in range(1, limit + 1):
        if x % i:
            state = False
            break
    
    return state

while True:
    if (x > 0) and multiple(x):
        print x
        break
    x += 2520

# оптимизировать делители
