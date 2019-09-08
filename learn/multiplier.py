from os import system

# MICHELIA'S
#     HAVE ROBO FUN     #
name = input('enter your name: ')
print('hello {0}'.format(name))
number1 = int(input("Enter a number \n"))
number2 = int(input("Enter another number\n"))
for num in range (1 , number2 +1 ):
    nummy = number1 * num
    print('{0} * {1} = {2}'.format(number1,num,nummy ))
