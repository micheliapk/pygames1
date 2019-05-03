#michelia's python playground****************
#num = [8,5,3]
#num = [3, 1, 2]
#num=[11100989089080211, 1122001231231, 1121389798646546546565465]
num = [12, 6, 4, 3]
#print(num[0])

my_len = len(num)


for count in range (0,my_len):
    if num[0] > num[count]:
        num.insert(count + 1, num[0])
        del num[0]
print('List1 ==> {}'.format(num))

for count in range (1,my_len):
    if num[1] > num[count]:
        num.insert(count + 1, num[1])
        del num[1]

print('List2 ==> {}'.format(num))

for count in range (1,my_len):
    if num[2] > num[count]:
        num.insert(count + 1, num[2])
        del num[2]

print('List3 ==> {}'.format(num))

for count in range (1,2):
    if num[3] > num[count]:
        num.insert(count + 1, num[3])
        del num[3]



print('List4 ==> {}'.format(num))
if num[0]>num[2]:
    num.insert(0,num[2])
    del num[3]

if num[1]>num[2]:
    num.insert(3,num[1])
    del num[1]

print('List ==> {}'.format(num))
print('Len ==> {}'.format(len(num)))

#for count in range (1,my_len):
#   print (num[count])

print('Sorted List ==> {}'.format(num))

