import search as hands
import re
import distribute as db

#for debug
#hand = ['2','2','JOKER','3','2']

i = 0
j = 1
check = 0
card_check = []
straight_flash_check = []
num_list = [int(s) for s in db.num]
num_list.sort()

#for debug of royal straight flush
#card_list = ['10', '2' ,'3', '4' , '5']

#for debug of role
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

#for debug of role
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

for no in num_list :
    straight_flash_check.append(no)
if jor_check :
    if int(straight_flash_check[1]) == int(straight_flash_check[4]) - 3 :
        check = 11
else :
    if int(straight_flash_check[0]) == int(straight_flash_check[4]) - 4 :
        check = 12
