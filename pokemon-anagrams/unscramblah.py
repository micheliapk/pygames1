
import random


def scramble_word(word):
    return ''.join(random.sample(word, len(word)))

my_words = ["dragonair","scyther","glacion","umbreon","espion",
            "goldeen","seel","sylveon","vaporeon"]

#choose the secret word index
secret_word_index = random.randint(0, len(my_words)-1)

#get the secret word from the list
secret_word = my_words[secret_word_index]

#scramble the secret word
scrambled_word = scramble_word(secret_word)

print (scrambled_word)

answer = input('Enter the unscrambled name: ')

if answer == secret_word:
    print('Awesome')
else:
    print('Try harder next time!')
     
