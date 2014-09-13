#!/usr/bin/python2.7

s = 'azcbobobegghakl'

def count(s):
    vowels = 'aeiouAEIOU'
    c = 0

    for char in s:
        if char in vowels:
            c += 1

    return c

print "Number of vowels: ", count(s)
