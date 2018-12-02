import num_check as pair

no = pair.check

if no == 0 :
    role = 'no role...'
elif no == 1 :
    role = 'one pair!'
elif no == 2 :
    role = 'two pair!'
elif no == 3 :
    role = 'three card!'
elif no == 4 :
    role = 'full house!!'
elif no == 6 :
    role = 'four card!!'
elif no == 10 :
    role = 'five card!!'
elif no == 11 :
    role = 'Straight Flush with JORKER!!!'
elif no == 12 :
    role = 'Straight Flush!!!'

comment = 'You have ' + role
print(comment)
