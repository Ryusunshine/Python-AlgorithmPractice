# 백준 2480

dice = list(map(int, input().split(' ')))
price = 0
for j in range(len(dice)):
    if len(set(dice)) == 1:
        print(dice[j] * 1000 + 10000)
        break
    elif dice[j] in dice[j+1:]:
        print(dice[j] * 100 + 1000)
        break
    else:
        print(max(dice) * 100)
        break


