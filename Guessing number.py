# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:47:54 2020

@author: Joy
"""

import random

play_game = 'y'

while play_game=='y':
    answer = random.randint(1,100)
    try_number = int(input('Guess a number between 1 and 100: '))
    counter=1
    
    while try_number != answer:
        if try_number>answer:
            print('Number is too large')
        if try_number<answer:
            print('Number is too small')
        counter+=1
        try_number = int(input('Guess a number between 1 and 100: '))
    print("You got it in ", str(counter), ' tries')
    play_game = input('Continue: ')
    if play_game == 'n': 
        print('Thanks for playing') 
        break
        