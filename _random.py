import random

names = ['ali','enes','ismail','yusuf']

# result = names[random.randint(0,len(names)-1)]

# result = random.choice(names)

# liste = list(range(10))
# random.shuffle(liste)
# result = liste

liste = range(100)
result = random.sample(liste, 3)




print(result)