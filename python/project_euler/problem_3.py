#!/usr/bin/python2.7
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

x = 600851475143
y = 2
z = 0

def isSimple(x):
    state = True

    for i in range(2, x):
        if not x % i:
            state = False
            break

    return state

while y < int(math.sqrt(x)):
    if (not x % y) and (isSimple(y)) and (y > z):
       z = y
    y += 1

print z


# Optimizirovat isSimple s vydeleniem pamyati
