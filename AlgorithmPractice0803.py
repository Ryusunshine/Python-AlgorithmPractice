import queue
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split(' '))
graph = [list(map(str, input())) for _ in range(r)]

# 상하좌우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
word = []
word.append(graph[0][0])
visited = [[False] * m for _ in range(n)]


def bfs(graph, visited, r, c, d):
    global result
    visited[r][c] = True
    queue.append([r, c, graph[r][c]])
    while queue:
        r, c, step = queue.popleft()
        result = max(result, len(step))

        for i in range(len(d_col)):
            next_row = d_row[i] + r
            next_col = d_col[i] + c
            if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > m-1:
                continue
            if visited[next_row][next_col]:
                continue
            if graph[next_row][next_col] in word:
                continue
            step.append(graph[next_row][next_col])
            visited[next_row][next_col] = True
            queue.append(next_row, next_col, step + graph[next_row][next_col] )

result = []
bfs(graph, visited, n, m, 1, word)
print(visited)
result.append(''.join(word))
print(result)
max_result = 0
for i in range(len(result)):
    if len(result[i]) > max_result:
        max_result = len(result[i])
print(max_result)
