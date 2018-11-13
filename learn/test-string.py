from os import system

# MICHELIA'S
#     HAVE ROBO FUN     #
def talk(words):
    system('say {0}'.format(words))

#test_word = 'bananas'
test_word = input('enter your favorite word: ')
print(test_word[0])
print(len(test_word))