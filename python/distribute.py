import random
import trump

i = 0
kind = ['JORKER']
player, cpu, num, player_num, cpu_num, remainder, remainder_num = [], [], [], [], [], [], []

for card in trump.cards :
    j = 0 
    while j < 13 :
        kind.append(card + ' ' + str(trump.cards[card][j]))
        j += 1

while len(num) < 20 :
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
        elif len(num) < 10 :
            cpu.append(kind[rand])
            cpu_num.append(rand)
        else :
            remainder.append(kind[rand])
            remainder_num.append(rand)
        num.append(rand)
        
#See what you and cpu have
print("player : %s" % player)
print("player_num : %s" % player_num)
print("cpu : %s" % cpu)
print("cpu_num : %s" % cpu_num)
print("remainder : %s" % remainder)
print("remainder_num : %s" % remainder_num)
#print(num)
