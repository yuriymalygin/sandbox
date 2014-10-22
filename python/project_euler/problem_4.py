#!/usr/bin/python2.7
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

p = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        z = str(x * y)
        if (z[:len(z)/2] == z[len(z)/2:][::-1]) and (z > p):
            p = z
print p
