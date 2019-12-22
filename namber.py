import random
import math

#
PC_rendom = random.randint(1, 50)
# modul=0
# tryID = 0
kol_raz = 0
#
while kol_raz < 6:
    user_variant = input()
##
    modul = math.fabs(int(user_variant) - PC_rendom)
    # print(f'число:  {PC_rendom} ')
    if int(user_variant) == PC_rendom:
        print('УГАДАЛ!!!!!УРААААА!!!')
        break
    else:
        kol_raz = kol_raz + 1
        altog = 6 - kol_raz

        if altog < 1:
            print(f'жаль конечно, вы были так близки, правильное число: {PC_rendom}')
            break
        elif modul >= 20:
            print(f'очень холодно 20, еще остались {altog} попытok')
            continue
        elif modul >= 10:
            print(f'холодно 10, еще остались {altog} попытok')
            continue
        elif modul >= 5:
            print(f'тепло 5, еще остались {altog} попытok')
            continue
        elif modul >= 2:
            print(f'горячо 2, еще остались {altog} попытok')
            continue
        elif modul == 1:
            print(f'очень очень!!!!!! +-1, еще остались {altog} попытok')
            continue
        print(f' еще остались {altog} попытok')
###