#!/usr/bin/python2.7
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

x = y = z = p = 0

def palindrome(x):

    if (not len(x) % 2 and 
        (x[0] == x[-1]) and 
        (x[1] == x[-2]) and 
        (x[2] == x[-3])):
        return True
    else:
        return False

for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        if (len(str(z)) == 6) and palindrome(str(z)) and (z > p):
            p = z
print p
