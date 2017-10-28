from os import system
from random import uniform

def talk(words):
    system('say {0}'.format(words))


def get_float(min_number, max_number):
    float_number = uniform(min_number, max_number)

    #print float number below
    print('Before rounding : {0} '.format(float_number))

    #round the number to two decimals
    float_number = round(float_number, 2)

    # print float number below
    print('After rounding : {0} '.format(float_number))

    return float_number

#get_float(max_number=10)
operator = '+'
questions_count = 0
if operator == '+':
    top_number = get_float(4,8)
    bottom_number = get_float(2,4)
    correct_answer = top_number + bottom_number
    correct_answer = round(correct_answer, 2)

print_question = '{0}:   ${1} {2} ${3} = ?'.\
                format(questions_count, top_number, operator, bottom_number)
print(print_question)

#TODO: talk_currency(5.67, 2.2, '+') ==> ('what is 5 dollars and 67 cents plus 2 dollars and 2 cents ')
input_string = input(': $ ')
try:
    student_answer = float(input_string)
except:
    talk('Do not enter junk values. Enter a valid number')
print('student_answer is {0}'.format (student_answer))

if correct_answer == student_answer:
    print('You are correct')
else:
    print('You are wrong. The correct answer is {0}'.format(correct_answer))

