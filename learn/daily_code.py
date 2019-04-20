#WELCOME TO MICHELIA'S DAILY CODE

print('Hi, what is your name !')

name_string = input()

print('{0}, what is your age?'.format(name_string))
age_string = input()

print('you are {0} '.format (age_string))


age = int(age_string)

year = 2019
birth_date =(year-age)
if age <= 2 or age > 110 :
    print('Ha ha!Good joke!!!')
    print('I am smarter than you think')
print(' you were born in {0}'.format(birth_date))

if age == 9 :
    print('Hey! You are the same age as me!!')