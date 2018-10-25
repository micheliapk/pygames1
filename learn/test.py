from os import system

# MICHELIA'S
#     HAVE ROBO FUN     #
def talk(words):
    system('say {0}'.format(words))

name = input('Hiker 1: Hi there, what is your name ?')
print('Nice to meet you, {0}'.format(name))

gender = input('Hiker 2: Can you also tell if you are a boy or girl')

if gender.lower() == 'boy':
    pronoun = 'him'
else:
    pronoun = 'her'

print('Hiker 1:what is this animal !')
print('Hiker 2: Lets ask {0}. Whenever you ask {1}, tell ...what is your favorite animal ?'.format(name, pronoun))
animal = 'animal'
print (animal)
animal_1 = input('Hiker 1:{0} ,what is your favorite animal ?'.format(name, pronoun))
print('{0}\'s favorite animal is {1}'.format(name, animal_1))