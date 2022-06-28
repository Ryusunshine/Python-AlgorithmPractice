from collections import deque

n, k = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
s, x, y = map(int, input().split(' '))
print(s, x, y)
visited = [[False] * n for _ in range(n)]

# 오른쪽 왼쪽 위 아래
d_row = [0, 0, -1, 1]
d_col = [1, -1, 0, 0]

if graph[x-1][y-1] != 0:
    print(graph[x-1][y-1])
else:
    print('0')

