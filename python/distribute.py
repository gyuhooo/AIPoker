import random
import trump

i = 0
kind = ['JORKER']
player = []
cpu = []
num = []
player_num = []

for card in trump.cards :
    j = 0
    while j < 13 :
        kind.append(card + ' ' + str(trump.cards[card][j]))
        j += 1

while len(num) < 10 :
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
        if len(num) < 5 :
            player.append(kind[rand])
            player_num.append(rand)
        else :
            cpu.append(kind[rand])
        num.append(rand)
#See what you and cpu have
print("player : %s" % player)
print("cpu : %s" % cpu)
#print(num)
