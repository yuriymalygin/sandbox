#!/usr/bin/python2.7
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def check(a,b,c,x):
    state = False

    if (a + b + c == x) and (a < b < c) and (a**2 + b**2  == c**2):
        state = True

    return state

def triplet(x):
    for a in xrange(0, x):
        for b in xrange(0, x):
            for c in xrange(0, x):
                if check(a,b,c,x):
                    return a, b, c

print triplet(1000)
