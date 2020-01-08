import random

################Имена кто первый начинает? #######################
name1 = input('Первое имя игрока: ')
name2 = input('Второе имя игрока: ')
players = [name1, name2]
pal = int(input('ввод количества палочек: '))  # количество палок, стартовый ввод значения
print(f'Итак, игра началась, выбрано: {pal} палочек!')
choice_Who = random.choice(players)
if choice_Who == name1:
    print(f"Первый вытягивает {name1}")
    turn_players = [name1, name2]
else:
    print(f"Первый вытягивает {name2}")
    turn_players = [name2, name1]


##############################################################
# Вводные данные:

while pal > 1:
    #Игроки по очереди тянут палки
    Rule1_3 = 1
    for name in turn_players:

        while Rule1_3 == 1:
            input_number_player = int(input('сколько палочек вытянуть:'))
            if pal >= 4:
                if input_number_player < 1 or input_number_player > 3:
                    print("Введите правильное значение от 1-3")
                    Rule1_3 = 1
                elif input_number_player >= 1 and input_number_player <= 3:
                    print('правило 1-3 выполнено')
                    Rule1_3 = 0  # ввод заканчивается и выходим из цикла коректировки 1-3
            if pal == 3:
                if input_number_player == 3 or input_number_player > 3:
                    print("Введите допустимое значение от 1-2")
                    Rule1_3 = 1
                elif input_number_player >= 1 and input_number_player <= 2:
                    Rule1_3 = 0
                else:
                    print("Е/ Введите допустимое значение от 1-2")
                    Rule1_3 = 1
            if pal == 2:
                if input_number_player == 3:
                    print("вы можете вытянуть только 1 палочку")
                    Rule1_3 = 1
                elif input_number_player == 2:
                    print("вы можете вытянуть только 1 палочку")
                    Rule1_3 = 1
                elif input_number_player == 1:

                    Rule1_3 = 0  # ввод заканчивается и выходим из цикла коректировки 1-1
                    print(f"Віиграл 1111 {name}")
                    break
                else:
                    print("вы можете вытянуть только 1 палочку")
                    Rule1_3 = 1
            #if pal == 1:  # на всякий случай
                #    print(' Если палок 1 /проиграл игрок:')
                #    print(name)
            #    break
        pal = pal - input_number_player
        print(f'произвели отнимание и остаток:{pal}')

        if pal <= 1:
            print('выиграл')
            print(name)
            break


        else:
            print(f'остаток:{pal}')
            print(f'тянул:{name}')
            Rule1_3=1
            continue

