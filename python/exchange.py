import distribute as db
import random


flag = [False, False, False, False, False]

def click(no) :
    if flag[no] :
        flag[no] = False
    else :
        flag[no] = True

def redistr() :
    i = 0
    for fl in flag :
        while(fl == True) :
            rand = random.randint(0, 9)
            if db.remainder[rand] != 0 :
                db.player[i] = db.remainder[rand]
                db.player_num[i] = db.remainder_num[rand]
                db.remainder[rand] = 0
                fl, flag[i] = False, False
            elif db.remainder == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] :
                fl, flag[i] = False, False
                break
            else :
                continue
        
        i += 1
    print(db.remainder)
    print(db.player)
