#michelia's python playground****************
colors = ['navy','purple','aqua','lavender']

print (colors[1]) #question 3

#question 4
colors[0] = 'pink'

#question 5
del colors[2]

#question 6
colors.append('red')
print (colors)
#question 7
colors.insert(0, 'blue')
print(colors)

spell_list= [
    {
        'word':'ending',
        'part_of_speech': 'noun',
        'meaning': 'the last part of anything'
    },
    {
        'word':'house',
        'part_of_speech': 'noun',
        'meaning': 'a building for people to live in'
    },

    {
        'word':'kindly',
        'part_of_speech': 'adj',
        'meaning': 'friendly'
    },
    {
        'word':'relax',
        'part_of_speech': 'verb',
        'meaning': 'to rest'
    },

    {
        'word': 'bacon',
        'part_of_speech': 'noun',
        'meaning': 'meat from the sides of a pig that has been salted and smoked'
    },
    {
        'word': 'radar',
        'part_of_speech': 'noun',
        'meaning': 'a radio device or system for locating an object'
    },

    {
        'word': 'globe',
        'part_of_speech': 'noun',
        'meaning': 'a round ball that has the map of the earth drawn on it'
    },
    {
        'word': 'yak',
        'part_of_speech': 'noun',
        'meaning': 'a large blackish brown ox with long wavy hair that is used for its milk '
                   'and meat and to carry heavy loads  '
    },

    {
        'word': 'hobby',
        'part_of_speech': 'noun',
        'meaning': 'any favorite activity or interest'
    },
    {
        'word': 'markers',
        'part_of_speech': 'plural noun',
        'meaning': 'things placed to serve as a guide or to indicate position'
    },
]

word_num_string = input('please enter a number between 0 to 9: ')
word_num = int(word_num_string)

print(spell_list[word_num])














