#!/usr/bin/python2.7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

def is_simple(x):
    state = True

    for i in range(2, x):
        if not x % i:
            state = False
            break

    return state

def n_simple(x):
    p = [2]
    i = 3

    while len(p) < x:
        if is_simple(i) and (i > int(p[-1])):
           p.extend([i])
           print len(p)
        i += 1
    
    return p

print n_simple(10001)
