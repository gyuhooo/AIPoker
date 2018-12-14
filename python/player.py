import num_check as pair
import distribute as db

def role_comment():
    
    no = pair.check(db.player, db.player_num)
    
    if no == 0 :
        role = 'no role...'
    elif no == 1 :
        role = 'one pair!'
    elif no == 2 :
        role = 'two pair!'
    elif no == 3 :
        role = 'three card!'
    elif no == 4 :
        no = 8        
        role = 'full house!!'
    elif no == 5 :
        role = 'Straight!!'
    elif no == 6 :
        no = 9
        role = 'four card!!'
    elif no == 10 :
        no = 12
        role = 'five card!!!'
    elif no == 7 :
        role = 'Flush!!'
    elif no == 11 :
        role = 'Straight Flush!!!'
    elif no == 13 :
        role = 'Royel Straight Flash!!!!'

    comment = 'You have ' + role
    
    return comment 

def player_role() :
    no = pair.check(db.player, db.player_num)
    return no