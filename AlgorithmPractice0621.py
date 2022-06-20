# 볼링공 조합 구하기

from itertools import combinations
n, m = map(int, input().split(' '))
number = list(map(int, input().split(' ')))

result = list(combinations(number, 2))
new_result = []
for i in result:
    if i[0] != i[1]:
        new_result.append(i)
print(len(new_result))


# 