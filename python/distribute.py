import random
import trump

i = 0
kind = ['JORKER']
distribute = []
num = []

for card in trump.cards :
    j = 0
    while j < 13 :
        kind.append(card + ' ' + str(trump.cards[card][j]))
        j += 1

while len(num) < 5 :
    flag = True
    rand = random.randint(0,52)
    for no in num :
        if no == None :
            break
        if no == rand :
            flag = False
            break
        i += 1
    
    if flag :
        num.append(rand)
        distribute.append(kind[rand])

#See what you have
print(distribute)
#print(num)