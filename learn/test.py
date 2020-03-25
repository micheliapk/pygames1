

print('What date were you born?')
date = input()

try:
    date = int(date)
except:
    print('🤬')
    exit(0)

if date < 1 or date > 31  :
        print('🤯')
else:
    print('👍')


a = "1000"
b = "02"
print(a + b)

c = 1000
d = 2
print(c - d)

if c < d :
    print('C is Less than D.')
else:
    print('C is greater than  or equal to  D')

if a < b :
    print('A is Less than B.')
else:
    print('A is greater than equal B')
