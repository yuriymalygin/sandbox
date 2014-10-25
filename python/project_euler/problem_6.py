#!/usr/bin/python2.7
#
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

def square_difference(x):
    s = y = 0

    for i in range(1, x+1):
        s += i**2 
        y += i 

    return abs(s - y**2)

print square_difference(100)
