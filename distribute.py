import random
import trump
i = 0
kind = ['JORKER']

for card in trump.cards :
    j = 0
    while j < 13 :
        kind.append(card + ' ' + str(trump.cards[card][j]))
        j += 1

while i < 5 : 
    print(kind[random.randint(0,52)])
    i += 1
