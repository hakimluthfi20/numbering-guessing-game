# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 06:43:35 2022

@author: muhammad luthfi hakim
"""

import random

guessesUsed = 0

print("welcome to the numbering guessing game")
Name = input('Hello! What is your name? ')
number = random.randint(1, 30)

print('Hi, ' + Name + ', I\'m thinking of a number between 1 and 30.')
while guessesUsed < 3:

    guess = int(input('Guess the number within 5 guesses: '))
    guessesUsed = guessesUsed + 1
    
    if guess < number:
        print('Too low, try again.')
    if guess > number:
        print('Too high, try again.')
    if guess == number:
        break

if guess == number:
        guessesUsed = str(guessesUsed)
        print('Well done, ' + Name + '! You guessed correctly in ' + guessesUsed + ' guesses.')
        
if guess != number:
        number = str(number)

print('Sorry, out of guesses. The number I was thinking of is ' + number)