#!/usr/bin/python2.7
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def triplet(x):
    for a in xrange(0, x):
        for b in xrange(0, x):
            if (a < b < (x - a - b)) and (a**2 + b**2  == (x - a - b)**2):
                return a * b * (x - a - b)

print triplet(1000)
