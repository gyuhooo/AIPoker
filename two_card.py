import search as hands

#デバッグ用
#hand = [2,2,2,3,2]

i = 0
j = 1
check = 0
card_check = []

#デバッグ用
#for num in hand :

for num in hands.hand :
    card_check.append(num)
    while (j <= i) :
        if card_check[i-j] == card_check[i] :
            check += 1
        j += 1

        #デバッグ用
        #print('j : ' + str(j))

    j = 1
    i += 1

    #デバッグ用
    #print('i : ' + str(i))

print(check)