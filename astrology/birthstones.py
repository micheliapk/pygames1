# Michelia's python playground
print("What is your name ?")
name = input()
print("Hello {0}".format(name))

print("What is the month you were born ?")
month = input().lower()

#if month == 'january':
    #print("Your birthstone is a Garnet,they were believed to have medicinal powers in the medeival times.")
#else :
    #if month == 'february':
     #print("Your birthstone is an Amethyst, Greeks believed it prevented getting drunk.")
#if month == 'march':
     #print("Your birthstone is an Aquamarine, sailors have worn aquamarine to ward off seasickness.")
#else :
    #if month == 'april':
     #print("Your birthstone is a Diamond, the ancient Romans and Greeks believed that diamonds were tears cried by the gods.")
     #print("That's the same as me!")
#if month == 'may':
     #print("Your birthstone is an Emerald, folklore stated that putting an emerald under your tongue would make it possible to see the future.")
#else :
    #if month == 'june':
     #print("Your birthstone is an Alexandrite, many myths and legends describe alexandrite as a carrier of good luck.")
#if month == 'july':
     #print("Your birthstone is a Ruby, Rubies symbolize power and protection.")
#else :
    #if month == 'august':
     #print("Your birthstone is a Sardonyx, the Greeks considered this stone to serve them as a source of courage. ")
#if month == 'september':
     #print("Your birthstone is a Sapphire, Europeans in the Middle Ages believed that sapphires cured eye disease.")
#else :
    #if month == 'october':
     #print("Your birthstone is a Tourmaline, in the medeival ages people used tourmaline to heal emotional ailments.  ")
#if month == 'november':
     #print("Your birthstone is a Citrine, it has been believed to promote creativity.")
#else :
    #if month == 'december':
     #print("Your birthstone is a Turquoise, in the ancient Persian Empire, turquoise was worn around the neck or wrist to help protect one’s self from unnatural death.")


stone = {
    'january': 'Your birthstone is a Garnet,they were believed to have medicinal powers in the medeival times.',
    'february': 'Your birthstone is an Amethyst, Greeks believed it prevented getting drunk.',
    'march': 'Your birthstone is an Aquamarine, sailors have worn aquamarine to ward off seasickness.',
    'april': 'Your birthstone is a Diamond, the ancient Romans and Greeks believed that diamonds were tears cried by the gods.',
    'may': 'Your birthstone is an Emerald, folklore stated that putting an emerald under your tongue would make it possible to see the future',
    'june': 'Your birthstone is an Alexandrite, many myths and legends describe alexandrite as a carrier of good luck.',
    'july': 'Your birthstone is a Ruby, Rubies symbolize power and protection.',
    'august': 'Your birthstone is a Sardonyx, the Greeks considered this stone to serve them as a source of courage.',
    'september': 'Your birthstone is a Sapphire, Europeans in the Middle Ages believed that sapphires cured eye disease',
    'october': 'Your birthstone is a Tourmaline, in the medeival ages people used tourmaline to heal emotional ailments.',
    'november': 'Your birthstone is a Citrine, it has been believed to promote creativity.',
    'december': 'Your birthstone is a Turquoise, in the ancient Persian Empire, turquoise was worn around the neck or wrist to help protect one’s self from unnatural death.'

        }
print (stone[month])








