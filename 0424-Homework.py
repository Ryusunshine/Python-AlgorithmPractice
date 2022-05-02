# 문제 1

n,m = list(map(int, input().split(' ')))
cards = [list(map(int, input())) for _ in range(n)]

max_value = 0
for i in range(n):
    min_row = min(cards[i]) # 각 행을 돌면서 리스트에서 최소값끼리 비교해서 큰 수를 찾는다
    if min_row > max_value:
        max_value = min_row
print(max_value)

# 문제 2
location = input()
location = [int(location[1]), ord(location[0])-96]


d_col = [-2, -2, 2, 2, -1, -1, 1, 1]
d_row = [-1, 1, -1, 1, 2, -2, -2, 2]
count = 0

for i in range(len(d_row)):
    next_row = location[0] + d_row[i]
    next_col = location[1] + d_col[i]
    if next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8:
        continue
    count += 1
print(count)


# 문제 4

n, k = list(map(int, input().split(' ')))
count = 0
if n < k:
    print('n이 커야합니다')
while True:
    if n == 1:
        break
    elif n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

# 문제 5
coin_list = [500, 100, 50, 10]
coin_num = 0
n = int(input())
if n % 10 != 0:
    print('10의 배수가 아닙니다')
else:
    for coin in coin_list:
        coin_num += int(n / coin)
        n %= coin
print(coin_num)
