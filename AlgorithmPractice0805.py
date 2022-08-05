# 백준 1987

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split(' '))
graph = [list(map(str, input())) for _ in range(n)]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

def bfs():
    queue = set()
    global result
    queue.add((0, 0, graph[0][0]))
    while queue:
        r, c, step = queue.pop()
        result = max(result, len(step))
        for i in range(len(d_col)):
            next_row = d_row[i] + r
            next_col = d_col[i] + c
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m:
                continue
            if graph[next_row][next_col] in step:
                continue
            queue.add((next_row, next_col, step + graph[next_row][next_col]))

result = 0
bfs()
print(result)

