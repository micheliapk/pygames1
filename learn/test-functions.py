from os import system



def multigo(myInt):
    for i in range (1,16):
        #"Only going up to fifteen"
        answer = myInt * i
        print('{0} x {1} = {2}'.format(myInt, i, answer))

mult_number = int (input('Please type multiplying number ? '))

multigo(mult_number)
