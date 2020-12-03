# Automatic Dice Roller
# Written by [your name]

import random

question = input('Would you like to roll the dice [y/n]?\n')

while question != 'n':
    if question == 'y': #questions are prints requireing a input after 
        die = random.randint(1, 6) #sets range from 1-6
        print(die)  #print a number 1-6
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".') #prints a statement
        question = input('Would you like to roll the dice [y/n]?\n')        

print('Good-bye!')
