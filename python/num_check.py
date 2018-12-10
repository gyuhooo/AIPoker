import search as hands
import re
import distribute as db

def check() :

    i = 0
    j = 1
    check = 0
    card_check = []
    straight_flash_check = []
    num_list = [int(s) for s in db.player_num]
    num_list.sort()
    hand = hands.search()
    
    for num in hand :
        card_check.append(num)
        while (j <= i) :
            if card_check[i-j] == card_check[i] :
                check += 1
            j += 1
            
        j = 1
        i += 1

    hd = str(hand)
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

    return check
        
"""
for no in num_list :
    straight_flash_check.append(no)
if jor_check :
    if int(straight_flash_check[1]) == int(straight_flash_check[4]) - 3 :
        check = 11
else :
    if int(straight_flash_check[0]) == int(straight_flash_check[4]) - 4 :
        check = 12
"""
