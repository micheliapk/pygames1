from os import system
from random import uniform

def talk(words):
    system('say {0}'.format(words))


def get_float(max_number):
    float_number = uniform(0, max_number)

    #print float number below
    print('Before rounding : {0} '.format(float_number))

    #round the number to two decimals
    float_number = round(float_number, 2)

    # print float number below
    print('After rounding : {0} '.format(float_number))

    return float_number

get_float(max_number=10)