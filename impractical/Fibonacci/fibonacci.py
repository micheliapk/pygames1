# Welcome, to the Fibonacci Program
n = int(input('Choose a number between 1 and 1000:'))

# Iteration 1
a = 1
b = 1
c = a + b
print(a)
print(b)
print(c)
# Iteration 2
# a = b
# b = c
# c = a + b
# print(c)

for i in range (3,n):
    a = b
    b = c
    c = a + b
    print(c)