from builtins import min
x, k = map(int, input().split(' '))

def reindex(i, move):
    if i > len(move):
        i = i - len(move)
        return i


result = []


def dfs(x, k):
    location = x
    move = [+1, -1, *2]
    second = 0

    while True:
        if location == k:
            result.append(second)
            break

        for i in move:
            i = reindex(i, move)
            location = location + i
            second += 1
            dfs(x, k)

dfs(x, k)
find_smallest = 1e9
for i in range(len(result)):
    if find_smallest > result[i]:
        find_smallest = result[i]
print(find_smallest)
