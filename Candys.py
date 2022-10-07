def CandysGame():
    from random import randint
    order = randint(1,2)
    print(order, "-й игрок ходит первым")
    cnds = 2021
    player1 = 0
    player2 = 0
    move = 1
    while cnds > 0:
        if move % 2 == 1 and order == 1 or move % 2 == 0 and order == 2:
            print("Ход первого игрока:")
            a = int(input())
            if a > 28 or a < 0:
                print("Можно взять не более 28 конфет")
                continue
            if a <= cnds:
                player1 += a
                print("Конфет у первого игрока: ", player1)
                cnds -=a
                print("Осталось конфет:", cnds)
                move += 1
                a = 0
            else:
                print("нет такого количества конфет")
                a=0
                continue
        else:
            print("Ход второго игрока:")
            a = int(input())
            if a > 28 or a < 0:
                print("Можно взять не более 28 конфет")
                continue
            if a <= cnds:
                player2 += a
                print("Конфет у второго игрока: ", player2)
                cnds -=a
                print("Осталось конфет:", cnds)
                move += 1
                a = 0
            else:
                print("нет такого количества конфет")
                a=0
                continue
    if (move + order) % 2 == 1:
        print("Победил первый игрок")
    else:
        print("Победил второй игрок")
    
def CandysGameBot():
    from random import randint
    order = randint(1,2)
    print(order, "-й игрок ходит первым")
    cnds = 2021
    player1 = 0
    player2 = 0
    move = 1
    while cnds > 0:
        if move % 2 == 1 and order == 1 or move % 2 == 0 and order == 2:
            print("Ход первого игрока:")
            a = int(input())
            if a > 28 or a < 0:
                print("Можно взять не более 28 конфет")
                continue
            if a <= cnds:
                player1 += a
                print("Конфет у первого игрока: ", player1)
                cnds -=a
                print("Осталось конфет:", cnds)
                move += 1
                a = 0
            else:
                print("нет такого количества конфет")
                a=0
                continue
        else:
            print("Ход второго игрока:")
            if cnds <= 28:
                a = cnds
            elif cnds > 57:
                a = 28
            else:
                a = cnds - 29
            print("Второй игрок берёт", a)    
            player2 += a
            print("Конфет у второго игрока: ", player2)
            cnds -=a
            print("Осталось конфет:", cnds)
            move += 1
            a = 0
            
    if (move + order) % 2 == 1:
        print("Победил первый игрок")
    else:
        print("Победил второй игрок")
    
#CandysGame()
CandysGameBot()