# 백준 9037

def process():
    n, candy = int(input()), list(map(int, input().split(' ')))
    cnt = 0
    while not check(n, candy): # 같아지는 경우에만 멈추기
        cnt += 1
        candy = teacher(n, candy)
    print(cnt)

def check(n, candy):
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1
        return len(set(candy)) == 1

def teacher(n, candy):
    tmp_list = [0 for _ in range(n)]
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1
        tmp_list[(i+1) % n] = candy[i] #오른쪽에 줄값은 내가 가진값의 절반
        candy[i] //= 2 # 그리고 내꺼는 절반으로 나눈다.

    for i in range(n):
        candy[i] += tmp_list[i]
    return candy

for i in range(int(input())):
    process()

# 백준 17224

import sys
input = sys.stdin.readline
n, l, k = map(int, input().split(' '))
test = [list(map(int, input().split(' '))) for _ in range(n)]
score = 0
cnt = 0
for i in range(len(test)):
    if cnt == k:
        break
    if max(test[i]) <= l: # 둘다 작은경우
        score += 140
        cnt += 1
    elif test[i][0] <= l:
            score += 100
            cnt += 1
    else:
        continue

print(score)
















