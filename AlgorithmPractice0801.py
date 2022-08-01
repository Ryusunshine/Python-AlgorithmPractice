# 백준 5585 거스름돈

coin = [500, 100, 50, 10, 5, 1]
coin.sort(reverse=True)
money = int(input())
change = 1000 - money

count = 0

for i in coin:
    if change % i < 0:
        continue
    mok = change // i
    count += mok
    change -= i * mok

print(count)

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

# 오름차순 정렬 수행
array.sort()

#불만도의 합 계산
result = 0
for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1])
print(result)

