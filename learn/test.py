from os import system

# MICHELIA'S
#     HAVE ROBO FUN     #
def talk(words):
    system('say {0}'.format(words))

def gugudan_master(q,w):
    print('I answer gugudan questions !!!')
    return(q * w)

answer = gugudan_master( 100,37 )
print('{0} * {1} = {2}'.format(100, 37, answer))
#q = 4  *  w  = 3
    # |
    # *
name = input('Please type your name:')
name =name.lower()

if name .lower() ==  'michelia':
    print('Hi we have the same name!!! ', name)
else:
    print(' Hi ', name)


age = int(input('Please type your age:'))

if age ==  7:
    print('Hi we are the same age!!! ' )
else:
    print(' Hi ' )
    if age <= 0 or age > 120:
        print('You are a liar')
    elif age <= 6:
        print('You are younger than me')

    elif age == 7:
        print('My age is 7 too')
    elif age >= 60:
        print('Hello grandparent ! ! !')
    elif age >= 8:
        print('You are older than me')

























