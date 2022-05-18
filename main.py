# 볼링공 무게 문제

n, m = map(int, input().split(' '))
weight_list = list(map(int, input().split(' ')))

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if weight_list[i] == weight_list[j]:
            count += 1
result = int((n * (n-1)) / 2) - count
print(result)