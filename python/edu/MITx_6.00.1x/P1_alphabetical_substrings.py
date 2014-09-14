#!/usr/bin/python2.7

s = 'azcbobobegghakl'

def longest_substring(s):
    ss_begin = 0
    ss_end = 0

    for position in range(0,len(s)):
        start_position = stop_position =position
        while stop_position < len(s) - 1:
            if s[stop_position] <= s[stop_position + 1]:
                stop_position += 1
            else:
                break
        if ss_end - ss_begin < stop_position - start_position:
            ss_begin = start_position
            ss_end = stop_position

    return  s[ss_begin:ss_end + 1]

print "Longest substring in alphabetical order is:", longest_substring(s)
