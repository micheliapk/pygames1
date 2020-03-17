# Michelia's python playground
print("What is your name ?")
name = input()
print("Hello {0}".format(name))

print("What is the month you were born ?")
month = input().lower()

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
print('What date were you born?')
date = input()
if month == 'january':
    if date <= '19' :
        print('Your star sign is Capricorn! A fun fact about it, is that Capricorns love to keep people guessing !')

if month == 'january':
    if date >= '20':
        print('Your star sign is Aquarius! A fun fact about it, is that Aquarius can get bored easily...')

if month == 'february':
    if date <= '18':
        print('Your star sign is Aquarius! A fun fact about it, is that Aquarius can get bored easily...')

if month == 'february':
    if date >= '19':
        print('Your star sign is Pisces! A fun fact about it, is that Pisces looks sweet and shy but they have a very wild side too!')
if month == 'march':
    if date <= '20':
        print('Your star sign is Pisces! A fun fact about it, is that Pisces looks sweet and shy but they have a very wild side too!')
if month == 'march':
    if date >= '21':
        print('Your star sign is Aries! Your actions tell an Aries everything they need to know about you!')
if month == 'april':
    if date <= '19':
        print('Your star sign is Aries! Your actions tell an Aries everything they need to know about you.!')
    else:
        print('Your star sign is Taurus! A fun fact is that though people often think of it as a rampaging bull it is actually quite kind!')
if month == 'may':
    if date <= '20':
        print(
            'Your star sign is Taurus! A fun fact is that though people often think of it as a rampaging bull it is actually quite kind!')
    else:
        print('Your star sign is Gemini! It doesn’t take much to make a Gemini happy, but it takes even less to make them mad...')

if month == 'june':
    if date <= '20':
        print(
            'Your star sign is Gemini! It doesn’t take much to make a Gemini happy, but it takes even less to make them mad...')
    else:
        print('Your star sign is Cancer, Cancer’s phrase is “I feel”. ')
if month == 'july':
    if date <= '22':
        print('Your star sign is Cancer, Cancer’s phrase is “I feel”. ')
    else:
        print('Your star sign is Leo ,Leo is a great friend because they often defend those who can’t defend themselves. ')

if month == 'august':
    if date <= '22':
        print('Your star sign is Leo ,Leo is a great friend because they often defend those who can’t defend themselves. ')
    else:
        print('Your star sign is Virgo ,Virgo and music can never be separated')

if month == 'september':
    if date <= '22':
        print('Your star sign is Virgo! A fun fact about it, is that Virgo is extremely trustworthy')
    else:
        print('Your star sign is Libra! A fun fact about it, is that Libra are shy until you get to know them.')

if month == 'october':
    if date <= '22':
        print('Your star sign is Libra! A fun fact about it, is that Libra are shy until you get to know them.')
    else:
        print('Your star sign is Scorpio! Scorpio can be overly protective of those they love.')

if month == 'november':
    if date <= '23':
        print('Your star sign is Scorpio! Scorpio can be overly protective of those they love.')
    else:
        print('Your star sign is Sagittarius! Sagittarius are quite clever in getting what they want.')

if month == 'december':
    if date <= '23':
        print('Your star sign is Sagittarius! Sagittarius are quite clever in getting what they want.')
    else:
        print('Your star sign is Capricorn! Capricorn always bounces back.')

monthdays = {
    'january': (1,31),
    'february': (1,29),
    'march': (1,31),
    'april': (1,30),
    'may': (1,31),
    'june': (1,30),
    'july': (1,31),
    'august': (1,31),
    'september':(1,30),
    'october': (1,31),
    'november': (1,30),
    'december':(1,31)

        }




print('what is your favorite color')
color = input().lower()

colors = {
    'red': 'The color red is able to boost energy! Red can also increase a person’s appetite.',
    'orange': 'Orange is aggressive but balanced — it portrays energy yet can be inviting',
    'yellow': 'Yellow is associated with laughter, hope and sunshine.',
    'green': 'Green symbolizes health, new beginnings and wealth.',
    'blue': 'Seeing the color blue causes the body to create chemicals that are calming.',
    'purple': 'Purple is associated with mystery, creativity, royalty and wealth.',
    'pink': 'Pink is inherently sweet, cute and charming.',
    'brown': 'Brown creates a sense of stability and support.',
    'black': ' Black is strong, bold and has a little touch of mystery',
    'white': 'White evokes purity and innocence.',
    'gray': 'Gray is a more mature, responsible color.',
        }
print (colors[color])
