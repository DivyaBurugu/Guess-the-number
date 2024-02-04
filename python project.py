#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sridi
#
# Created:     24-01-2022
# Copyright:   (c) sridi 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
secretnumber=random.randint(1,25)
print(' i am thinking of a number between 1 and 25.')
for guessestaken in range (1,8):
    print("take a guess.")
    guess=int(input())
    if guess<secretnumber:
        print('your guess is too low.')
    elif guess>secretnumber:
        print('your guess is too high.')
    elif guess==secretnumber:
        print('good job!.')
        break
