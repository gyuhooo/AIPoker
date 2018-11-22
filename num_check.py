import search as hands
import re

#for debug
#hand = ['2','2','JOKER','3','2']

i = 0
j = 1
check = 0
card_check = []

#for debug
#for num in hand :

for num in hands.hand :
    card_check.append(num)
    while (j <= i) :
        if card_check[i-j] == card_check[i] :
            check += 1
        j += 1

        #for debug
        #print('j : ' + str(j))

    j = 1
    i += 1

    #for debug
    #print('i : ' + str(i))

#for debug
#print(check)

hd = str(hands.hand)
repatter = re.sub("\W'|',|'|]", '', hd)
jor_check = re.search('JORKER', repatter)
if (check == 0) and jor_check :
    check += 1
elif (check == 1) and jor_check :
    check += 2
elif (check == 2) and jor_check :
    check += 2
elif (check == 3) and jor_check :
    check += 3
elif (check == 6) and jor_check :
    check += 4
