#michelia's python playground****************
#num = [8,5,3]
#num = [3, 1, 2]
#num=[11100989089080211, 1122001231231, 1121389798646546546565465]
num = ['xfftdztfyhtj', 'bftycxfxd', 'gyfhtd']
#print(num[0])

if num[0] > num[1]:
    num.insert(2,num[0])
    del num[0]

if num[0]>num[2]:
    num.insert(0,num[2])
    del num[3]

if num[1]>num[2]:
    num.insert(3,num[1])
    del num[1]

print('List ==> {}'.format(num))
print('Len ==> {}'.format(len(num)))

#for count in range (0,len(num)):
#    print (num[count])

print('Sorted List ==> {}'.format(num))

