#michelia's python playground****************
#num = [8,5,3]
#num = [3, 1, 2]
#num=[11100989089080211, 1122001231231, 1121389798646546546565465]
#num = [12, 6, 4, 3, 5]
num=['elephants','lunch','can','ants','for','eat']

#print(num[0])

my_len = len(num)

# for count1 in range(0,len(num)):
#     for count2 in range(0,len(num) ):
#         for count3 in range(0, len(num)):
#           print('count:',count1, count2, count3)


def swap(index1, index2):
    # Swap the number[index1] to number[index2]

    bin = num[index1]
    num[index1] = num[index2]
    num[index2] = bin

print('Unsorted List0 ==> {}'.format(num))
for outer_count in range(0, my_len - 1):
    for count in range (outer_count + 1,my_len):
        if num[outer_count] > num[count]:
            print('count = {}'.format(count))
            swap(outer_count, count)



#    for count in range (1,my_len - 1):
#       if num[1] > num[count]:
#           swap(1,count)
#
# print('List2 ==> {}'.format(num))
#
# for count in range (2,my_len):
#    if num[2] > num[count]:
#        swap(2,count)
#
# print('List3 ==> {}'.format(num))



print('Sorted List ==> {}'.format(num))

