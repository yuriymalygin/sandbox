#!/usr/bin/python2.7
'''
Bisection Search
x = 83
100 / 2 = 50 ? Low
(100 - 50)/2 + 50 = 75 ? Low
(100 - 75)/2 + 75 = 87 ? High
(87 - 75)/2 + 75 = 81 ? Low
(87 - 81)/2 + 81 = 84 ? High
(84 - 81)/2 + 81 = 82 ? Low
(84 - 82)/2 + 82 = 83 ? Yes
'''

# Vars
limit = 100
min_guess = 0
guess = limit/2
answer = None

# Body
print "Please think of a number between 0 and 100!"

while answer != 'c':
    print "Is your secret number " +str(guess) + "?"
    answer = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if answer == 'l':
        min_guess = guess
        guess = guess + (limit - guess)/2
    elif answer == 'h':
        limit = guess
        guess = min_guess + (limit - min_guess)/2
    elif answer == 'c':
        print "Game over. Your secret number was: ", guess
        break
    else:
        print "Sorry, I did not understand your input."
