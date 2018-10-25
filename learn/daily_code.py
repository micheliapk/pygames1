# HI! MICHELIA,WELCOME TO YOUR DAILY PRACTICE! #

print('Hi, what is your name !')

name_string = input()

print('How are you {0}'.format (name_string))


print('Hi, what is your age?')
age_string = input()

print('you are {0}'.format (age_string))


age = int(age_string)

year = 2018
birth_date =(year-age)
if age <= 0 or age > 120:
    print('Ha ha!Good joke!!!')
print('You were born in {0}'.format(birth_date))