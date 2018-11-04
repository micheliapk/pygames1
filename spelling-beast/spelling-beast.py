from os import system
from random import randint

from datetime import datetime


def get_current_time():
    return datetime.now()


def is_5_minutes_done(start_time):
    current_time = get_current_time()
    return ((current_time - start_time).total_seconds()) / 60 >= 5


def get_percent_score(questions_count, score):
    return (score * 100) / questions_count


def talk(words):
    system('say {0}'.format(words))


print('**** Welcome to Michelia\'s Spelling Beast!!!')
talk('Welcome to Mikaylias Spelling Beast!')
talk('How do you spell  the word ending ?')
word_string = input()
if word_string  == 'ending':
    print('You are correct')
    talk('You are correct')
else:
    print('You are wrong. This word is spelled like E N D I N G' )
    talk('You are wrong. This word is spelled like E N D I N G')

spell_list= [
    {
      'house':'a building that people live in','noun',''

}
]
