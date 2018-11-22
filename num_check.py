import search as hands

#for debug
#hand = [2,2,2,3,2]

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

print(check)
