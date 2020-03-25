#pokes = [ 'Vulpix', 'Ivysaur','Pikachu', 'Rhyhorn', 'Lapras','Ekans',
              # 'Raichu', 'Staryu', 'Tentacool', 'Golbat', 'Snorlax']



#type(pokes)

#pokemon = pokes[3]

#pokemon[3] # 'Rhyhorn'

#pokemon[3:7] # 'horn'

#p2 = pokes [2]

#p2[0:4] # 'Pika'


friends = ['Charlotte','Sprihaa','Siyi','Caitlyn']
print(friends)
print('Traitor!! I do not need Caitlyn anymore!!')
del friends[3]
print (friends)
print('Nithya is nice she can replace Caitlyn!!')
friends.append('Nithya')
print(friends)
friends.pop()
print(friends)
friends.insert(-1,'Nithya')
print(friends)

print('___________________________________________')
buddy = ('Charlotte','Sprihaa','Caitlyn','Siyi','Nithya')
bud1 = buddy[0:2] + buddy [3:5]
bud2 = buddy[:-3] + buddy[-2:]
#budie = bud + buddy[3:5]
print(bud1)
print(bud2)
print()
sa,aa,ss = '11','22','33'
print(sa + aa + ss)
print(ss)

name = input('Enter your name: ')
sunsign=input('Enter your sunsign: ')
sent = '%s\'s star sign is %s !!' %(name, sunsign)
print(sent)