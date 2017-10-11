from os import system
from random import randint

def talk(words):
    system('say {0}'.format(words))

def number_guesser():
    pass

def you_guess():
    answer = randint(1, 100)

    guess = None

    while guess != answer :
        guess = int (input('Please type your guess number ? '))
        if answer <  guess :
            print('answer is less than your guess')
        elif answer > guess:
             print('answer is greater than your guess')
        elif answer == guess:
             print('answer is correct')

#you_guess()

def find_mean (q,w):
    mean = (q + w) / 2
    return mean

my_mean = find_mean(50,100)
print('mean is {0}'.format(my_mean))
