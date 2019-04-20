from os import system

# MICHELIA'S
#     HAVE ROBO FUN     #
def talk(words):
    system('say {0}'.format(words))

test_word ='bananas'
test_word = input('enter your favorite word: ')
#print(test_word[1])
print('Length is {0}'.format(len(test_word)))
test_word_len =len(test_word)

for number in range (test_word_len):
    print(test_word[number])

# print(test_word[0])
# print(test_word[1])
# print(test_word[2])
# print(test_word[3])
# print(test_word[4])
# print(test_word[5])
# print(test_word[6])
