import search as hands
import re
import distribute as db

def check(dist, dist_num) :

    i = 0
    j = 1
    flash_check, check = 0, 0
    card_check = []
    num_list = [int(s) for s in dist_num]                   
    num_list.sort()
    hand = hands.search(dist)
    
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

    for suit in dist_num:    

        if 1 <= suit <= 13:
            tmp = 1
        elif 14 <= suit<=26:
            tmp = 2
        elif 27 <= suit <=39:
            tmp = 3
        elif 40 <= suit <=52:
            tmp = 4 

        if flash_check == 0:
            kind = tmp
            flash_check = 1
            continue 

        if tmp == kind:
            flash_check += 1
    """
    j = 1
    pattern = '.*?(\d+)'
    card_str = str(card_check)
    repatter = re.sub("\W'|',|'|]", '', card_str)
    #l_si_i = [int(s) for s in repatter]
    car_ch = re.findall(pattern, repatter)
    card_check_num = [int(s) for s in car_ch]
    card_check_num.sort()
    straight_check = 0
    while (j < 5) :
        if card_check_num[4] == card_check_num[4 - j] + j :
            straight_check += 1
        j += 1
    """
    if (flash_check == 5) or ((flash_check == 4) and jor_check) :
        if check <= 3 :
            check = 7
        """if (straight_check == 4) ((straight_check == 3) and jor_check) :
            if check <= 10 :
                check = 11
    elif (straight_check == 4) ((straight_check == 3) and jor_check) :
        if check <= 3 :
            check = 5
    
    straightflash_check = dist_num
    straightflash_check.sort()

    if straightflash_check == [48, 49, 50, 51, 52] :
        check = 13
    """
    return check 