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
    global flag
    for fl in flag :
        while(fl == True) :
            rand = random.randint(0, 9)
            ran = rand
            if db.remainder[ran] != 0 :
                db.player[i] = db.remainder[ran]
                db.player_num[i] = db.remainder_num[ran]
                db.remainder[ran] = 0
                db.remainder_num[ran] = 0
                fl, flag[i] = False, False
            elif db.remainder == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] :
                fl, flag[i] = False, False
                break
            else :
                continue
        
        i += 1
