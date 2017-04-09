from os import system
from random import randint

try:
    from PIL import Image
except:
    print('**** Try installing Pillow image module using \"pip install Pillow\" '
	  'or \"python3 -m pip install Pillow\"')

animal_list = [ 'Vulpix', 'Ivysaur','Pikachu', 'Rhyhorn', 'Lapras','Ekans',
                'Raichu', 'Staryu', 'Tentacool', 'Golbat', 'Snorlax']

clues = {
    'Vulpix': ['It is brown', 'It has many tails'],
    'Ivysaur': ['It is blue', 'It is very big if you evolve'],
    'Pikachu': ['It is yellow', 'It is very powerful'],
    'Rhyhorn': ['It is gray', 'It is strong'],
    'Lapras': ['It is blue', 'It lives in water'],
    'Ekans': ['It is purple', 'It is long'],
    'Raichu': ['It is brown', 'It is very powerful'],
    'Staryu': ['It is yellow', 'It lives in water'],
    'Tentacool': ['It is blue', 'It lives in water'],
    'Golbat': ['It is blue', 'It can fly'],
    'Snorlax': ['Its belly is white', 'It is very big']
    }

def talk(words):
    system('say {0}'.format(words))

#for animal in animal_list:
#    talk(animal)

secret_animal_number = randint(0, len(animal_list)-1)
secret_animal = animal_list[secret_animal_number]
solved = False

print('**** Welcome to Michelia\'s PokeMon Game ***')
print('****** Please guess the secret animal ******')
talk('Please guess the secret animal')
for anim in range(len(animal_list)):
    print('[{0}] {1}'.format(anim, animal_list[anim]))

for number in range(3):
    talk('Enter the animal number: ')
    input_string = input('Enter the animal number: ')

    try:
        answer = int(input_string)
    except:
        talk('Hi baby, please do not enter junk values. Enter a valid number')
        continue

    if answer == secret_animal_number:
        talk('you are CORRECT, Genius!')
        
        solved = True
        break
    elif number < 2:
        talk ("Sorry, Please try AGAIN. Heres a clue")
        talk (clues[secret_animal][number])

if solved == True:
    talk('Bye Bye')
else:
    talk('Sorry, the secret animal is {0}'.format(secret_animal))

image = Image.open('images/{0}.png'.format(secret_animal))
image.show()


#talk('the secret animal is {0}'.format(animal))

#talk('good night me kelia and naveen')
#talk('dinoasaur supercalifragilisticexpialidocious blahblah')
#talk('happy halloween oooooohhchhhhh zzzzzzzz')
#talk('I am going to tell you a spooky scary story')
#talk('its christmas!')

