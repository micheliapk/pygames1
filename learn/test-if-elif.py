#michelia's python playground

print('Tell me your age!')
age_string = input()

age = 0

try:
    age = int(age_string)
except:
    print('Do not enter junk values. Enter a valid number')
    exit(0)

if age <= 0 or age > 120:
    print('You are a liar')
elif age == 7:
    print('My age is 7 too')

elif age >= 8:
    print('You are older than me')
elif age <= 6:
    print('You are younger than me')


























