#!/usr/bin/python2.7

s = 'azcbobobegghakl'

def count(s):
    pattern = 'bob'
    position = 0
    c = 0

    for char in s:
        position = s.find(pattern, position)
        if position >= 0:
            c += 1
            position +=1

    return c

print "Number of times bob occurs is:", count(s)
