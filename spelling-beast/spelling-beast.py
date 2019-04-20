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

spell_list_g1 = [
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
        'word': 'boasted',
        'part_of_speech': 'verb',
        'meaning': 'said or told something intended to give others a high opinion of yourself : bragged'
    },

    {
        'word': 'prayer',
        'part_of_speech': 'noun',
        'meaning': 'an address (such as a petition or confession) to God or a god in word or thought'
    },
    {
        'word': 'tireless',
        'part_of_speech': 'adj',
        'meaning': 'seemingly not able to become weary or have your strength decrease or fail'
    },

    {
        'word': 'factory',
        'part_of_speech': 'noun',
        'meaning': 'a building or collection of buildings with facilities (such as machines) for making goods often '
                   'from raw materials'
    },
    {
        'word': 'borrowed',
        'part_of_speech': 'verb',
        'meaning': ' received something (such as a book) from a library to use outside the library for a period of time'

    },

    {
        'word': 'shavings',
        'part_of_speech': 'plural noun',
        'meaning': 'thin strips of wood pared off by a tool for smoothing or shaping wood'
    },

    {
        'word': 'poodles',
        'part_of_speech': 'plural noun',
        'meaning': 'dogs of an old European breed of active, intelligent dogs that have a curly, dense, '
                   'solid-colored coat and are grouped into standard, miniature and toy sizes'
    },
#71
    {
        'word': 'gravity',
        'part_of_speech': 'noun',
        'meaning': 'the tendency or state of being drawn to the mass of something in the sky (such as the earth, '
                   'the moon or a planet) for bodies at or near its surface'
    },
    {
        'word': 'abnormal',
        'part_of_speech': 'adj',
        'meaning': 'differing from the typical'
    },

    {
        'word': 'sneakers',
        'part_of_speech': 'plural noun',
        'meaning': 'shoes usually of canvas with flexible rubber soles worn especially for sports or hiking'
    },
    {
        'word': 'crackle',
        'part_of_speech': 'verb',
        'meaning': 'to make small, sharp, sudden noises repeatedly'
    },

    {
        'word': 'inspire',
        'part_of_speech': 'verb',
        'meaning': 'to encourage or motivate'
    },
    {
        'word': 'pleats',
        'part_of_speech': 'plural noun',
        'meaning': 'folds in cloth made by doubling material over on itself and that is stitched, attached or held '
                   'along one side.'
    },

    {
        'word': 'shivery',
        'part_of_speech': 'adj',
        'meaning': 'rigid, cold'
    },
    {
        'word': 'briefing',
        'part_of_speech': 'noun',
        'meaning': 'the process of being given usually essential information typically in little time and without'
                   ' unnecessary details '
    },

    {
        'word': 'obtain',
        'part_of_speech': 'verb',
        'meaning': 'to gain possession or disposal of usually by some planned action or method'
    },

    {
        'word': 'portray',
        'part_of_speech': 'verb',
        'meaning': 'to represent by drawing, painting or cutting something into the surface of a material'
    },
#81
    {
        'word': 'squeeze',
        'part_of_speech': 'verb',
        'meaning': 'to exert pressure especially on opposite sides or parts of : press together closely or tightly'
    },
    {
        'word': 'rumbling',
        'part_of_speech': 'verb',
        'meaning': 'making a low, heavy rolling sound'
    },

    {
        'word': 'gangplank',
        'part_of_speech': 'noun',
        'meaning': 'a long, narrow, movable platform or bridge used to get on or off a ship (as from a wharf)'
    },
    {
        'word': 'scratched',
        'part_of_speech': 'noun',
        'meaning': 'scraped or rubbed lightly with something pointed or rough in order to relieve itching'
    },

    {
        'word': 'distorted',
        'part_of_speech': 'verb',
        'meaning': 'twisted out of a natural, normal or original shape or condition'
    },
    {
        'word': 'cardboard',
        'part_of_speech': 'noun',
        'meaning': 'a stiff, thick kind of paper that sometimes has a coating and that can be used to make signs '
                   'or for printed material'
    },

    {
        'word': 'interviews',
        'part_of_speech': 'verb',
        'meaning': 'questions or talks with especially in order to gain information or learn personal qualities'
    },
    {
        'word': 'guilty',
        'part_of_speech': 'noun',
        'meaning': ' justly chargeable with or responsible for a fault or crime'

    },

    {
        'word': 'lunar',
        'part_of_speech': 'adj',
        'meaning': 'of, taking place on or relating to the moon'
    },

    {
        'word': 'custard',
        'part_of_speech': 'noun',
        'meaning': 'a sweetened mixture of milk and eggs that is baked, boiled or frozen'
    },
#91
    {
        'word': 'shriek',
        'part_of_speech': 'noun',
        'meaning': 'a shrill, usually wild or unintentional cry (as of sudden or extreme terror or pain or of violent'
                   ' laughter'
    },
    {
        'word': 'ghost',
        'part_of_speech': 'noun',
        'meaning': 'a supernatural appearance : apparition'
    },

    {
        'word': 'mission',
        'part_of_speech': 'noun',
        'meaning': 'a specific task with which a person or group is charged'
    },
    {
        'word': 'tempting',
        'part_of_speech': 'adj',
        'meaning': 'alluring, enticing'
    },

    {
        'word': 'majestic',
        'part_of_speech': 'adj',
        'meaning': 'having, exhibiting, or marked by magnificent or commanding power, effect, or appearance : regal'
    },
    {
        'word': 'solution',
        'part_of_speech': 'noun',
        'meaning': 'an answer to or a means of answering a problem : an explanation'
    },

    {
        'word': 'signals',
        'part_of_speech': 'plural noun',
        'meaning': 'sounds or gestures made to give warning or command'
    },
    {
        'word': 'eliminate',
        'part_of_speech': 'verb',
        'meaning': 'to get rid of'

    },

    {
        'word': 'universe',
        'part_of_speech': 'noun',
        'meaning': 'the entire celestial cosmos'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    }
]

spell_list_g2 = [
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
        'word': 'boasted',
        'part_of_speech': 'verb',
        'meaning': 'said or told something intended to give others a high opinion of yourself : bragged'
    },

    {
        'word': 'prayer',
        'part_of_speech': 'noun',
        'meaning': 'an address (such as a petition or confession) to God or a god in word or thought'
    },
    {
        'word': 'tireless',
        'part_of_speech': 'adj',
        'meaning': 'seemingly not able to become weary or have your strength decrease or fail'
    },

    {
        'word': 'factory',
        'part_of_speech': 'noun',
        'meaning': 'a building or collection of buildings with facilities (such as machines) for making goods often '
                   'from raw materials'
    },
    {
        'word': 'borrowed',
        'part_of_speech': 'verb',
        'meaning': ' received something (such as a book) from a library to use outside the library for a period of time'

    },

    {
        'word': 'shavings',
        'part_of_speech': 'plural noun',
        'meaning': 'thin strips of wood pared off by a tool for smoothing or shaping wood'
    },

    {
        'word': 'poodles',
        'part_of_speech': 'plural noun',
        'meaning': 'dogs of an old European breed of active, intelligent dogs that have a curly, dense, '
                   'solid-colored coat and are grouped into standard, miniature and toy sizes'
    },
#71
    {
        'word': 'gravity',
        'part_of_speech': 'noun',
        'meaning': 'the tendency or state of being drawn to the mass of something in the sky (such as the earth, '
                   'the moon or a planet) for bodies at or near its surface'
    },
    {
        'word': 'abnormal',
        'part_of_speech': 'adj',
        'meaning': 'differing from the typical'
    },

    {
        'word': 'sneakers',
        'part_of_speech': 'plural noun',
        'meaning': 'shoes usually of canvas with flexible rubber soles worn especially for sports or hiking'
    },
    {
        'word': 'crackle',
        'part_of_speech': 'verb',
        'meaning': 'to make small, sharp, sudden noises repeatedly'
    },

    {
        'word': 'inspire',
        'part_of_speech': 'verb',
        'meaning': 'to encourage or motivate'
    },
    {
        'word': 'pleats',
        'part_of_speech': 'plural noun',
        'meaning': 'folds in cloth made by doubling material over on itself and that is stitched, attached or held '
                   'along one side.'
    },

    {
        'word': 'shivery',
        'part_of_speech': 'adj',
        'meaning': 'rigid, cold'
    },
    {
        'word': 'briefing',
        'part_of_speech': 'noun',
        'meaning': 'the process of being given usually essential information typically in little time and without'
                   ' unnecessary details '
    },

    {
        'word': 'obtain',
        'part_of_speech': 'verb',
        'meaning': 'to gain possession or disposal of usually by some planned action or method'
    },

    {
        'word': 'portray',
        'part_of_speech': 'verb',
        'meaning': 'to represent by drawing, painting or cutting something into the surface of a material'
    },
#81
    {
        'word': 'squeeze',
        'part_of_speech': 'verb',
        'meaning': 'to exert pressure especially on opposite sides or parts of : press together closely or tightly'
    },
    {
        'word': 'rumbling',
        'part_of_speech': 'verb',
        'meaning': 'making a low, heavy rolling sound'
    },

    {
        'word': 'gangplank',
        'part_of_speech': 'noun',
        'meaning': 'a long, narrow, movable platform or bridge used to get on or off a ship (as from a wharf)'
    },
    {
        'word': 'scratched',
        'part_of_speech': 'noun',
        'meaning': 'scraped or rubbed lightly with something pointed or rough in order to relieve itching'
    },

    {
        'word': 'distorted',
        'part_of_speech': 'verb',
        'meaning': 'twisted out of a natural, normal or original shape or condition'
    },
    {
        'word': 'cardboard',
        'part_of_speech': 'noun',
        'meaning': 'a stiff, thick kind of paper that sometimes has a coating and that can be used to make signs '
                   'or for printed material'
    },

    {
        'word': 'interviews',
        'part_of_speech': 'verb',
        'meaning': 'questions or talks with especially in order to gain information or learn personal qualities'
    },
    {
        'word': 'guilty',
        'part_of_speech': 'noun',
        'meaning': ' justly chargeable with or responsible for a fault or crime'

    },

    {
        'word': 'lunar',
        'part_of_speech': 'adj',
        'meaning': 'of, taking place on or relating to the moon'
    },

    {
        'word': 'custard',
        'part_of_speech': 'noun',
        'meaning': 'a sweetened mixture of milk and eggs that is baked, boiled or frozen'
    },
#91
    {
        'word': 'shriek',
        'part_of_speech': 'noun',
        'meaning': 'a shrill, usually wild or unintentional cry (as of sudden or extreme terror or pain or of violent'
                   ' laughter'
    },
    {
        'word': 'ghost',
        'part_of_speech': 'noun',
        'meaning': 'a supernatural appearance : apparition'
    },

    {
        'word': 'mission',
        'part_of_speech': 'noun',
        'meaning': 'a specific task with which a person or group is charged'
    },
    {
        'word': 'tempting',
        'part_of_speech': 'adj',
        'meaning': 'alluring, enticing'
    },

    {
        'word': 'majestic',
        'part_of_speech': 'adj',
        'meaning': 'having, exhibiting, or marked by magnificent or commanding power, effect, or appearance : regal'
    },
    {
        'word': 'solution',
        'part_of_speech': 'noun',
        'meaning': 'an answer to or a means of answering a problem : an explanation'
    },

    {
        'word': 'signals',
        'part_of_speech': 'plural noun',
        'meaning': 'sounds or gestures made to give warning or command'
    },
    {
        'word': 'eliminate',
        'part_of_speech': 'verb',
        'meaning': 'to get rid of'

    },

    {
        'word': 'universe',
        'part_of_speech': 'noun',
        'meaning': 'the entire celestial cosmos'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    }
]

spell_list_g3 = [
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
        'word': 'boasted',
        'part_of_speech': 'verb',
        'meaning': 'said or told something intended to give others a high opinion of yourself : bragged'
    },

    {
        'word': 'prayer',
        'part_of_speech': 'noun',
        'meaning': 'an address (such as a petition or confession) to God or a god in word or thought'
    },
    {
        'word': 'tireless',
        'part_of_speech': 'adj',
        'meaning': 'seemingly not able to become weary or have your strength decrease or fail'
    },

    {
        'word': 'factory',
        'part_of_speech': 'noun',
        'meaning': 'a building or collection of buildings with facilities (such as machines) for making goods often '
                   'from raw materials'
    },
    {
        'word': 'borrowed',
        'part_of_speech': 'verb',
        'meaning': ' received something (such as a book) from a library to use outside the library for a period of time'

    },

    {
        'word': 'shavings',
        'part_of_speech': 'plural noun',
        'meaning': 'thin strips of wood pared off by a tool for smoothing or shaping wood'
    },

    {
        'word': 'poodles',
        'part_of_speech': 'plural noun',
        'meaning': 'dogs of an old European breed of active, intelligent dogs that have a curly, dense, '
                   'solid-colored coat and are grouped into standard, miniature and toy sizes'
    },
#71
    {
        'word': 'gravity',
        'part_of_speech': 'noun',
        'meaning': 'the tendency or state of being drawn to the mass of something in the sky (such as the earth, '
                   'the moon or a planet) for bodies at or near its surface'
    },
    {
        'word': 'abnormal',
        'part_of_speech': 'adj',
        'meaning': 'differing from the typical'
    },

    {
        'word': 'sneakers',
        'part_of_speech': 'plural noun',
        'meaning': 'shoes usually of canvas with flexible rubber soles worn especially for sports or hiking'
    },
    {
        'word': 'crackle',
        'part_of_speech': 'verb',
        'meaning': 'to make small, sharp, sudden noises repeatedly'
    },

    {
        'word': 'inspire',
        'part_of_speech': 'verb',
        'meaning': 'to encourage or motivate'
    },
    {
        'word': 'pleats',
        'part_of_speech': 'plural noun',
        'meaning': 'folds in cloth made by doubling material over on itself and that is stitched, attached or held '
                   'along one side.'
    },

    {
        'word': 'shivery',
        'part_of_speech': 'adj',
        'meaning': 'rigid, cold'
    },
    {
        'word': 'briefing',
        'part_of_speech': 'noun',
        'meaning': 'the process of being given usually essential information typically in little time and without'
                   ' unnecessary details '
    },

    {
        'word': 'obtain',
        'part_of_speech': 'verb',
        'meaning': 'to gain possession or disposal of usually by some planned action or method'
    },

    {
        'word': 'portray',
        'part_of_speech': 'verb',
        'meaning': 'to represent by drawing, painting or cutting something into the surface of a material'
    },
#81
    {
        'word': 'squeeze',
        'part_of_speech': 'verb',
        'meaning': 'to exert pressure especially on opposite sides or parts of : press together closely or tightly'
    },
    {
        'word': 'rumbling',
        'part_of_speech': 'verb',
        'meaning': 'making a low, heavy rolling sound'
    },

    {
        'word': 'gangplank',
        'part_of_speech': 'noun',
        'meaning': 'a long, narrow, movable platform or bridge used to get on or off a ship (as from a wharf)'
    },
    {
        'word': 'scratched',
        'part_of_speech': 'noun',
        'meaning': 'scraped or rubbed lightly with something pointed or rough in order to relieve itching'
    },

    {
        'word': 'distorted',
        'part_of_speech': 'verb',
        'meaning': 'twisted out of a natural, normal or original shape or condition'
    },
    {
        'word': 'cardboard',
        'part_of_speech': 'noun',
        'meaning': 'a stiff, thick kind of paper that sometimes has a coating and that can be used to make signs '
                   'or for printed material'
    },

    {
        'word': 'interviews',
        'part_of_speech': 'verb',
        'meaning': 'questions or talks with especially in order to gain information or learn personal qualities'
    },
    {
        'word': 'guilty',
        'part_of_speech': 'noun',
        'meaning': ' justly chargeable with or responsible for a fault or crime'

    },

    {
        'word': 'lunar',
        'part_of_speech': 'adj',
        'meaning': 'of, taking place on or relating to the moon'
    },

    {
        'word': 'custard',
        'part_of_speech': 'noun',
        'meaning': 'a sweetened mixture of milk and eggs that is baked, boiled or frozen'
    },
#91
    {
        'word': 'shriek',
        'part_of_speech': 'noun',
        'meaning': 'a shrill, usually wild or unintentional cry (as of sudden or extreme terror or pain or of violent'
                   ' laughter'
    },
    {
        'word': 'ghost',
        'part_of_speech': 'noun',
        'meaning': 'a supernatural appearance : apparition'
    },

    {
        'word': 'mission',
        'part_of_speech': 'noun',
        'meaning': 'a specific task with which a person or group is charged'
    },
    {
        'word': 'tempting',
        'part_of_speech': 'adj',
        'meaning': 'alluring, enticing'
    },

    {
        'word': 'majestic',
        'part_of_speech': 'adj',
        'meaning': 'having, exhibiting, or marked by magnificent or commanding power, effect, or appearance : regal'
    },
    {
        'word': 'solution',
        'part_of_speech': 'noun',
        'meaning': 'an answer to or a means of answering a problem : an explanation'
    },

    {
        'word': 'signals',
        'part_of_speech': 'plural noun',
        'meaning': 'sounds or gestures made to give warning or command'
    },
    {
        'word': 'eliminate',
        'part_of_speech': 'verb',
        'meaning': 'to get rid of'

    },

    {
        'word': 'universe',
        'part_of_speech': 'noun',
        'meaning': 'the entire celestial cosmos'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    }
]

spell_list_g4 = [
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
        'word': 'boasted',
        'part_of_speech': 'verb',
        'meaning': 'said or told something intended to give others a high opinion of yourself : bragged'
    },

    {
        'word': 'prayer',
        'part_of_speech': 'noun',
        'meaning': 'an address (such as a petition or confession) to God or a god in word or thought'
    },
    {
        'word': 'tireless',
        'part_of_speech': 'adj',
        'meaning': 'seemingly not able to become weary or have your strength decrease or fail'
    },

    {
        'word': 'factory',
        'part_of_speech': 'noun',
        'meaning': 'a building or collection of buildings with facilities (such as machines) for making goods often '
                   'from raw materials'
    },
    {
        'word': 'borrowed',
        'part_of_speech': 'verb',
        'meaning': ' received something (such as a book) from a library to use outside the library for a period of time'

    },

    {
        'word': 'shavings',
        'part_of_speech': 'plural noun',
        'meaning': 'thin strips of wood pared off by a tool for smoothing or shaping wood'
    },

    {
        'word': 'poodles',
        'part_of_speech': 'plural noun',
        'meaning': 'dogs of an old European breed of active, intelligent dogs that have a curly, dense, '
                   'solid-colored coat and are grouped into standard, miniature and toy sizes'
    },
#71
    {
        'word': 'gravity',
        'part_of_speech': 'noun',
        'meaning': 'the tendency or state of being drawn to the mass of something in the sky (such as the earth, '
                   'the moon or a planet) for bodies at or near its surface'
    },
    {
        'word': 'abnormal',
        'part_of_speech': 'adj',
        'meaning': 'differing from the typical'
    },

    {
        'word': 'sneakers',
        'part_of_speech': 'plural noun',
        'meaning': 'shoes usually of canvas with flexible rubber soles worn especially for sports or hiking'
    },
    {
        'word': 'crackle',
        'part_of_speech': 'verb',
        'meaning': 'to make small, sharp, sudden noises repeatedly'
    },

    {
        'word': 'inspire',
        'part_of_speech': 'verb',
        'meaning': 'to encourage or motivate'
    },
    {
        'word': 'pleats',
        'part_of_speech': 'plural noun',
        'meaning': 'folds in cloth made by doubling material over on itself and that is stitched, attached or held '
                   'along one side.'
    },

    {
        'word': 'shivery',
        'part_of_speech': 'adj',
        'meaning': 'rigid, cold'
    },
    {
        'word': 'briefing',
        'part_of_speech': 'noun',
        'meaning': 'the process of being given usually essential information typically in little time and without'
                   ' unnecessary details '
    },

    {
        'word': 'obtain',
        'part_of_speech': 'verb',
        'meaning': 'to gain possession or disposal of usually by some planned action or method'
    },

    {
        'word': 'portray',
        'part_of_speech': 'verb',
        'meaning': 'to represent by drawing, painting or cutting something into the surface of a material'
    },
#81
    {
        'word': 'squeeze',
        'part_of_speech': 'verb',
        'meaning': 'to exert pressure especially on opposite sides or parts of : press together closely or tightly'
    },
    {
        'word': 'rumbling',
        'part_of_speech': 'verb',
        'meaning': 'making a low, heavy rolling sound'
    },

    {
        'word': 'gangplank',
        'part_of_speech': 'noun',
        'meaning': 'a long, narrow, movable platform or bridge used to get on or off a ship (as from a wharf)'
    },
    {
        'word': 'scratched',
        'part_of_speech': 'noun',
        'meaning': 'scraped or rubbed lightly with something pointed or rough in order to relieve itching'
    },

    {
        'word': 'distorted',
        'part_of_speech': 'verb',
        'meaning': 'twisted out of a natural, normal or original shape or condition'
    },
    {
        'word': 'cardboard',
        'part_of_speech': 'noun',
        'meaning': 'a stiff, thick kind of paper that sometimes has a coating and that can be used to make signs '
                   'or for printed material'
    },

    {
        'word': 'interviews',
        'part_of_speech': 'verb',
        'meaning': 'questions or talks with especially in order to gain information or learn personal qualities'
    },
    {
        'word': 'guilty',
        'part_of_speech': 'noun',
        'meaning': ' justly chargeable with or responsible for a fault or crime'

    },

    {
        'word': 'lunar',
        'part_of_speech': 'adj',
        'meaning': 'of, taking place on or relating to the moon'
    },

    {
        'word': 'custard',
        'part_of_speech': 'noun',
        'meaning': 'a sweetened mixture of milk and eggs that is baked, boiled or frozen'
    },
#91
    {
        'word': 'shriek',
        'part_of_speech': 'noun',
        'meaning': 'a shrill, usually wild or unintentional cry (as of sudden or extreme terror or pain or of violent'
                   ' laughter'
    },
    {
        'word': 'ghost',
        'part_of_speech': 'noun',
        'meaning': 'a supernatural appearance : apparition'
    },

    {
        'word': 'mission',
        'part_of_speech': 'noun',
        'meaning': 'a specific task with which a person or group is charged'
    },
    {
        'word': 'tempting',
        'part_of_speech': 'adj',
        'meaning': 'alluring, enticing'
    },

    {
        'word': 'majestic',
        'part_of_speech': 'adj',
        'meaning': 'having, exhibiting, or marked by magnificent or commanding power, effect, or appearance : regal'
    },
    {
        'word': 'solution',
        'part_of_speech': 'noun',
        'meaning': 'an answer to or a means of answering a problem : an explanation'
    },

    {
        'word': 'signals',
        'part_of_speech': 'plural noun',
        'meaning': 'sounds or gestures made to give warning or command'
    },
    {
        'word': 'eliminate',
        'part_of_speech': 'verb',
        'meaning': 'to get rid of'

    },

    {
        'word': 'universe',
        'part_of_speech': 'noun',
        'meaning': 'the entire celestial cosmos'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    }
]

spell_list_g5 = [
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
        'word': 'boasted',
        'part_of_speech': 'verb',
        'meaning': 'said or told something intended to give others a high opinion of yourself : bragged'
    },

    {
        'word': 'prayer',
        'part_of_speech': 'noun',
        'meaning': 'an address (such as a petition or confession) to God or a god in word or thought'
    },
    {
        'word': 'tireless',
        'part_of_speech': 'adj',
        'meaning': 'seemingly not able to become weary or have your strength decrease or fail'
    },

    {
        'word': 'factory',
        'part_of_speech': 'noun',
        'meaning': 'a building or collection of buildings with facilities (such as machines) for making goods often '
                   'from raw materials'
    },
    {
        'word': 'borrowed',
        'part_of_speech': 'verb',
        'meaning': ' received something (such as a book) from a library to use outside the library for a period of time'

    },

    {
        'word': 'shavings',
        'part_of_speech': 'plural noun',
        'meaning': 'thin strips of wood pared off by a tool for smoothing or shaping wood'
    },

    {
        'word': 'poodles',
        'part_of_speech': 'plural noun',
        'meaning': 'dogs of an old European breed of active, intelligent dogs that have a curly, dense, '
                   'solid-colored coat and are grouped into standard, miniature and toy sizes'
    },
#71
    {
        'word': 'gravity',
        'part_of_speech': 'noun',
        'meaning': 'the tendency or state of being drawn to the mass of something in the sky (such as the earth, '
                   'the moon or a planet) for bodies at or near its surface'
    },
    {
        'word': 'abnormal',
        'part_of_speech': 'adj',
        'meaning': 'differing from the typical'
    },

    {
        'word': 'sneakers',
        'part_of_speech': 'plural noun',
        'meaning': 'shoes usually of canvas with flexible rubber soles worn especially for sports or hiking'
    },
    {
        'word': 'crackle',
        'part_of_speech': 'verb',
        'meaning': 'to make small, sharp, sudden noises repeatedly'
    },

    {
        'word': 'inspire',
        'part_of_speech': 'verb',
        'meaning': 'to encourage or motivate'
    },
    {
        'word': 'pleats',
        'part_of_speech': 'plural noun',
        'meaning': 'folds in cloth made by doubling material over on itself and that is stitched, attached or held '
                   'along one side.'
    },

    {
        'word': 'shivery',
        'part_of_speech': 'adj',
        'meaning': 'rigid, cold'
    },
    {
        'word': 'briefing',
        'part_of_speech': 'noun',
        'meaning': 'the process of being given usually essential information typically in little time and without'
                   ' unnecessary details '
    },

    {
        'word': 'obtain',
        'part_of_speech': 'verb',
        'meaning': 'to gain possession or disposal of usually by some planned action or method'
    },

    {
        'word': 'portray',
        'part_of_speech': 'verb',
        'meaning': 'to represent by drawing, painting or cutting something into the surface of a material'
    },
#81
    {
        'word': 'squeeze',
        'part_of_speech': 'verb',
        'meaning': 'to exert pressure especially on opposite sides or parts of : press together closely or tightly'
    },
    {
        'word': 'rumbling',
        'part_of_speech': 'verb',
        'meaning': 'making a low, heavy rolling sound'
    },

    {
        'word': 'gangplank',
        'part_of_speech': 'noun',
        'meaning': 'a long, narrow, movable platform or bridge used to get on or off a ship (as from a wharf)'
    },
    {
        'word': 'scratched',
        'part_of_speech': 'noun',
        'meaning': 'scraped or rubbed lightly with something pointed or rough in order to relieve itching'
    },

    {
        'word': 'distorted',
        'part_of_speech': 'verb',
        'meaning': 'twisted out of a natural, normal or original shape or condition'
    },
    {
        'word': 'cardboard',
        'part_of_speech': 'noun',
        'meaning': 'a stiff, thick kind of paper that sometimes has a coating and that can be used to make signs '
                   'or for printed material'
    },

    {
        'word': 'interviews',
        'part_of_speech': 'verb',
        'meaning': 'questions or talks with especially in order to gain information or learn personal qualities'
    },
    {
        'word': 'guilty',
        'part_of_speech': 'noun',
        'meaning': ' justly chargeable with or responsible for a fault or crime'

    },

    {
        'word': 'lunar',
        'part_of_speech': 'adj',
        'meaning': 'of, taking place on or relating to the moon'
    },

    {
        'word': 'custard',
        'part_of_speech': 'noun',
        'meaning': 'a sweetened mixture of milk and eggs that is baked, boiled or frozen'
    },
#91
    {
        'word': 'shriek',
        'part_of_speech': 'noun',
        'meaning': 'a shrill, usually wild or unintentional cry (as of sudden or extreme terror or pain or of violent'
                   ' laughter'
    },
    {
        'word': 'ghost',
        'part_of_speech': 'noun',
        'meaning': 'a supernatural appearance : apparition'
    },

    {
        'word': 'mission',
        'part_of_speech': 'noun',
        'meaning': 'a specific task with which a person or group is charged'
    },
    {
        'word': 'tempting',
        'part_of_speech': 'adj',
        'meaning': 'alluring, enticing'
    },

    {
        'word': 'majestic',
        'part_of_speech': 'adj',
        'meaning': 'having, exhibiting, or marked by magnificent or commanding power, effect, or appearance : regal'
    },
    {
        'word': 'solution',
        'part_of_speech': 'noun',
        'meaning': 'an answer to or a means of answering a problem : an explanation'
    },

    {
        'word': 'signals',
        'part_of_speech': 'plural noun',
        'meaning': 'sounds or gestures made to give warning or command'
    },
    {
        'word': 'eliminate',
        'part_of_speech': 'verb',
        'meaning': 'to get rid of'

    },

    {
        'word': 'universe',
        'part_of_speech': 'noun',
        'meaning': 'the entire celestial cosmos'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    },

    {
        'word': 'locusts',
        'part_of_speech': 'plural noun',
        'meaning': 'migratory grasshoppers that often travel in vast swarms and strip the areas they travel'
                   ' through of all vegetation.'
    }
]

print('**** Welcome to Michelia\'s Spelling Beast!!!')
talk('Welcome to Mikaylias Spelling Beast!')
secret_word_number = randint(0, len(spell_list_g3)-1)
secret_word = spell_list_g3[secret_word_number]

#print(secret_word['word'])

talk('How do you spell the word {0}'.format(secret_word['word']))
word_string = input()
if word_string  == secret_word['word']:
    print('You are correct')
    talk('You are correct')
else:
    print('You are wrong. This word is spelled like {0}'.format(secret_word['word']))
    talk('You are wrong. This word is spelled like {0}'.format(secret_word ['word']))


