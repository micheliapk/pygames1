from os import system
from random import randint

def talk(words):
    system('say {0}'.format(words))

answer = randint(1, 100)

guess = None

while guess != answer :
    guess = int (input('Guess ?'))
    if answer <  guess :
        print('answer is less than your guess')
    elif answer > guess:
         print('answer is greater than your guess')
    elif answer == guess:
         print('answer is correct')

