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

#11
    {
        'word': 'loaf',
        'part_of_speech': 'noun',
        'meaning': 'a shaped or molded lump of bread'
    },
    {
        'word': 'shiny',
        'part_of_speech': 'adj',
        'meaning': 'bright, glittering or polished'
    },

    {
        'word': 'disco',
        'part_of_speech': 'noun',
        'meaning': 'a type of popular dance music with strong steady rhythms and usually electronically produced sounds'
    },
    {
        'word': 'sloth',
        'part_of_speech': 'noun',
        'meaning': 'a slow-moving brownish or grayish mammal with very long front legs and long curved claws, '
                   'that hangs from branches and eats leaves and fruit'
    },

    {
        'word': 'maple',
        'part_of_speech': 'noun',
        'meaning': 'a tree with gray bark, sectioned leaves, hard wood and snap used to make syrup'
    },
    {
        'word': 'wary',
        'part_of_speech': 'adj',
        'meaning': 'cautious and on the look out for danger'
    },

    {
        'word': 'latch',
        'part_of_speech': 'verb',
        'meaning': 'to secure something against opening by using a device for holding it closed'
    },
    {
        'word': 'view',
        'part_of_speech': 'noun',
        'meaning': 'what you can see from a place'
    },

    {
        'word': 'toad',
        'part_of_speech': 'noun',
        'meaning': 'a small jumping animal similar to a frog but that spends more time on land and has rough, '
                   'dry, warty skin'
    },

#21
    {
        'word': 'family',
        'part_of_speech': 'noun',
        'meaning': 'a group of individuals living under one roof'
    },
    {
        'word': 'type',
        'part_of_speech': 'verb',
        'meaning': 'to write using a keyboard'
    },

    {
        'word': 'pudding',
        'part_of_speech': 'noun',
        'meaning': 'a sweet, creamy dessert that is soft, spongy or thick'
    },
    {
        'word': 'hours',
        'part_of_speech': 'plural noun',
        'meaning': 'periods of time lasting 60 minutes'
    },

    {
        'word': 'forest',
        'part_of_speech': 'noun',
        'meaning': 'a large area of land covered with lots of trees, shrubs and bushes'
    },
    {
        'word': 'moths',
        'part_of_speech': 'plural noun',
        'meaning': 'nsects that are similar to but less colorful than butterflies and that usually fly in the late evening or at night'
    },

    {
        'word': 'invent',
        'part_of_speech': 'verb',
        'meaning': 'to think up or imagine'
    },
    {
        'word': 'swoosh',
        'part_of_speech': 'verb',
        'meaning': 'to move with a rushing or rustling sound '

    },

    {
        'word': 'object',
        'part_of_speech': 'noun',
        'meaning': 'a thing that can be seen or touched'
    },

    {
        'word': 'plaster',
        'part_of_speech': 'noun',
        'meaning': 'a mix of usually sand, water and other materials that is used to coat inside walls and ceilings'
    },
#31
    {
        'word': 'lessons',
        'part_of_speech': 'plural noun',
        'meaning': 'classes taught on a single subject'
    },
    {
        'word': 'shrubs',
        'part_of_speech': 'plural noun',
        'meaning': 'plants that have woody stems and don\'t grow very tall'
    },

    {
        'word': 'otters',
        'part_of_speech': 'noun',
        'meaning': 'dark brown, aquatic, fish-eating mammals with long tails, short legs, webbed feet and small ears'
    },
    {
        'word': 'sapling',
        'part_of_speech': 'noun',
        'meaning': 'a young tree.'
    },

    {
        'word': 'tangled',
        'part_of_speech': 'adj',
        'meaning': 'knotted or twisted together'
    },
    {
        'word': 'quest',
        'part_of_speech': 'noun',
        'meaning': 'a journey to go in search of something'
    },

    {
        'word': 'wry',
        'part_of_speech': 'adj',
        'meaning': 'marked by a clever twist often with a hint of humor or sarcasm'
    },
    {
        'word': 'owner',
        'part_of_speech': 'noun',
        'meaning': 'omeone that has something that belongs to them'

    },

    {
        'word': 'pimple',
        'part_of_speech': 'noun',
        'meaning': 'a small, swollen and red spot on the skin'
    },

    {
        'word': 'orbit',
        'part_of_speech': 'noun',
        'meaning': 'to travel around something such as a planet in a curved path'
    },
#41
    {
        'word': 'birthday',
        'part_of_speech': 'noun',
        'meaning': 'an anniversary of the day someone was born'
    },
    {
        'word': 'royal',
        'part_of_speech': 'adj',
        'meaning': 'related to or owned by the family of a king or queen'
    },

    {
        'word': 'animals',
        'part_of_speech': 'plural noun',
        'meaning': 'any creatures except human beings'
    },
    {
        'word': 'presto',
        'part_of_speech': 'adj',
        'meaning': 'quickly, immediately'
    },

    {
        'word': 'splinter',
        'part_of_speech': 'noun',
        'meaning': 'a thin, sharp piece of something (like wood) that has broken off from a bigger piece'
    },
    {
        'word': 'wrong',
        'part_of_speech': 'adj',
        'meaning': 'not true, correct or right'
    },

    {
        'word': 'unicorn',
        'part_of_speech': 'noun',
        'meaning': 'an imaginary animal that has the body of a horse, the back legs of a stag, the tail of a lion'
                   'and a single horn in the middle of its head'
    },
    {
        'word': 'gremlin',
        'part_of_speech': 'noun',
        'meaning': 'a small, mischievous gnome that is imagined to cause errors or problems with equipment '
                   'and meat and to carry heavy loads  '
    },

    {
        'word': 'whenever',
        'part_of_speech': 'adj',
        'meaning': 'at any time'
    },

    {
        'word': 'garbage',
        'part_of_speech': 'noun',
        'meaning': 'trash of any kind'
    },
#51
    {
        'word': 'Fiji',
        'part_of_speech': 'noun',
        'meaning': 'an island country in the southwestern Pacific'
    },
    {
        'word': 'dense',
        'part_of_speech': 'adj',
        'meaning': 'crowded very close together'
    },

    {
        'word': 'groan',
        'part_of_speech': 'noun',
        'meaning': ' deep, sudden, unintentional sound that usually indicates pain, grief, or sometimes disapproval'
                   'or annoyance'
    },
    {
        'word': 'siren',
        'part_of_speech': 'noun',
        'meaning': 'an apparatus often electrically operated for producing a piercing warning sound of musical tones'
    },

    {
        'word': 'angles',
        'part_of_speech': 'plural noun',
        'meaning': 'the directions from which someone or something is viewed, considered or approached'
    },
    {
        'word': 'fend',
        'part_of_speech': 'verb',
        'meaning': 'to look out for oneself : manage'
    },

    {
        'word': 'rubbish',
        'part_of_speech': 'noun',
        'meaning': 'assorted useless, valueless waste or rejected matter : trash'
    },
    {
        'word': 'tuneful',
        'part_of_speech': 'adj',
        'meaning': 'having a musical sound : melodious '

    },

    {
        'word': 'artistic',
        'part_of_speech': 'adj',
        'meaning': 'characterized by taste and judgment or by art and skill'
    },

    {
        'word': 'squishy',
        'part_of_speech': 'adj',
        'meaning': 'being soft, yielding and damp'
    },
#61
    {
        'word': 'clumsy',
        'part_of_speech': 'adj',
        'meaning': 'not having ease in using the hands, skill, nimbleness or grace, such as in the use of the body'
                   'or limbs or in the performance of an action'
    },
    {
        'word': 'kibble',
        'part_of_speech': 'noun',
        'meaning': 'coarsely ground dried food products or grain'
    },

    {
        'word': 'cues',
        'part_of_speech': 'plural noun',
        'meaning': 'signals such as words or bits of stage business) to a performer to begin a specific speech'
                   'or action'
    },
    {
        'word': 'relax',
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
#71
    {
        'word': 'ending',
        'part_of_speech': 'noun',
        'meaning': 'the last part of anything'
    },
    {
        'word': 'house',
        'part_of_speech': 'noun',
        'meaning': 'a building for people to live in'
    },

    {
        'word': 'kindly',
        'part_of_speech': 'adj',
        'meaning': 'friendly'
    },
    {
        'word': 'relax',
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
#81
    {
        'word': 'ending',
        'part_of_speech': 'noun',
        'meaning': 'the last part of anything'
    },
    {
        'word': 'house',
        'part_of_speech': 'noun',
        'meaning': 'a building for people to live in'
    },

    {
        'word': 'kindly',
        'part_of_speech': 'adj',
        'meaning': 'friendly'
    },
    {
        'word': 'relax',
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
#91
    {
        'word': 'ending',
        'part_of_speech': 'noun',
        'meaning': 'the last part of anything'
    },
    {
        'word': 'house',
        'part_of_speech': 'noun',
        'meaning': 'a building for people to live in'
    },

    {
        'word': 'kindly',
        'part_of_speech': 'adj',
        'meaning': 'friendly'
    },
    {
        'word': 'relax',
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
    }

]

word_num_string = input('please enter a number between 0 to 60: ')
word_num = int(word_num_string)

print(spell_list[word_num])














