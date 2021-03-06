from os import system
from random import randint

from datetime import datetime

def get_current_time():
    return datetime.now()

def is_5_minutes_done(start_time):
    current_time = get_current_time()
    return ((current_time-start_time).total_seconds())/60 >= 5

def get_percent_score(questions_count, score):
    return (score*100)/questions_count
    
def talk(words):
    system('say {0}'.format(words))

print('**** Welcome to Michelia\'s Math Marathon !!!')
talk('Welcome to Mikaylias Math Marathon')

print('Enter 1 for Addition/Subtraction or 2 for Multiplication or 3 for all: ')
talk('hi, Do you want to do Addition or Subtraction or Multiplication or all')
input_string = input()

operation_input = 1

try:
    operation_input = int(input_string)
except:
    talk('Do not enter junk values. Enter a valid number')
    exit(0)

if operation_input == 1: #Addition
    operator = 'plus_minus'
    operator_name = 'plus_minus'
    total_questions = 100

elif operation_input == 2:#Multiplication
    operator = 'x'
    operator_name = 'times'
    total_questions = 25

elif operation_input == 3: # all
    operator = 'all'
    total_questions = 100

is_5mins_not_done = True
start_time = get_current_time()

questions_count = 0
score = 0
wrong_questions_list = [] #empty list to hold wrong questions

real_operator = operator
operator_list = ['+', '-', 'x']
operator_name_list = ['plus', 'minus', 'times']

while is_5mins_not_done == True and questions_count < total_questions:
    #test is not over. keep going

    questions_count += 1 # same as questions_count = questions_count + 1

    if real_operator == 'all':
        random_number = randint(0,2)
        operator = operator_list[random_number]
        operator_name = operator_name_list[random_number]
    elif real_operator == 'plus_minus':
        random_number = randint(0, 1)
        operator = operator_list[random_number]
        operator_name = operator_name_list[random_number]
    else:
        operator = real_operator

    if operator == '+':
        top_number = randint(9,30)
        bottom_number = randint(2, top_number if top_number > 2 else 8)
        correct_answer = top_number + bottom_number

    elif operator == '-':
        top_number = randint(9,30)
        bottom_number = randint(2, top_number if top_number > 2 else 8)
        correct_answer = top_number - bottom_number

    elif operator == 'x':
        top_number = randint(2,6)
        bottom_number = randint(0,12)
        correct_answer = top_number * bottom_number

    print_question = 'Question #{0}:  {1} {2} {3} = ?'.\
                format(questions_count, top_number, operator, bottom_number)
    print(print_question)

    question = 'what is {0} {1} {2}'.\
                format(top_number, operator_name, bottom_number)

    talk(question)
    input_string = input()
    try:
        student_answer = int(input_string)
    except:
        talk('Do not enter junk values. Enter a valid number')
        continue

    if student_answer == correct_answer:
        score += 1
        talk('Awesome')
    else:
        talk('Sorry TRY HARDER')
        wrong_questions_list.append(print_question)

    is_5mins_not_done = not is_5_minutes_done(start_time)

percent_score = int(get_percent_score(questions_count, score))
print('You scored {0} % ({1}/{2})'. format(percent_score, score, questions_count))
talk(' You scored {0} percent'.format (percent_score))

if wrong_questions_list:
    print('*** {0} Questions answered wrong ***\n'.format(len(wrong_questions_list)))
    print(wrong_questions_list)
