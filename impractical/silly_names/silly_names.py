import sys,random

print ('welcome,\n')
print('What a weird name !\n\n')

first = ('Dragonbreath','Missy','Fancy Nancy','Blabbermouth ','Mr.Peabody'
         ,'Mrs.Piggle Wiggle','Pignose','Jemmy of ',
         'Airhead','Loudmouth','Queeny Meany','Cuckoo Bird',
         'Tattle Tale Tom','Mommy Duncan','Tee Tee','Daddy Lara')

last = ('WXYZ','Register','Duck','Horny','Fagott','Atchoo','Burpy','Roller Koster',
        'Goober','Fizzlepop','Scrubby')

firstname = random.choice(first)
lastname = random.choice(last)

print ('\n\n')
print ('{} {}'.format(firstname, lastname),file = sys.stderr)
print('\n\n')


