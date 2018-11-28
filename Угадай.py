from random import randrange

my_namber = randrange(1,10)
not_bingo = True
bingo = 1

print("\nЯ загадываю число, а Вы пытаетесь отгадать с трёх раз! Поехали!  ")

while bingo and (bingo <=3):
    bingo += 1
    your_namber = input("Введите Ваше число " + str(bingo) + ":    ")
    if (int(my_namber) == my_namber):
        print("Bingo!!! Вы угадали моё число! Это равно: ", my_namber)
        break
    else:
        print("Вы не угадали. Мое число между", my_namber - 2, " и ",
                my_namber + 2)
else:
    print("К сожалению Вы не смогли в этот раз угадать заданное число. Попробуйте:  ")
