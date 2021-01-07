import random

comp = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
byk = 0
cow = 0
print(comp)
tryis = int(input('сколко раз вы хотите сыграть?: '))
count = 0
for j in range(tryis):
    if byk != 4:
        byk = 0
        cow = 0
    else:
        break
    count += 1
    player = list(map(int, input().split()))
    i = 0
    while i < 4:
        if comp[i] == player[i]:
            byk += 1
        elif comp[i] == player[0]:
            cow += 1
        elif comp[i] == player[1]:
            cow += 1
        elif comp[i] == player[2]:
            cow += 1
        elif comp[i] == player[3]:
            cow += 1
        i += 1
        if byk == 4:
            print('вы победили, кол-во попыток потребовалась:', count)
            break
    if byk != 4:
        print('вы не угадали попробуйте еще раз')
    print('корова ' + str(cow))
    print('бык ' + str(byk))
