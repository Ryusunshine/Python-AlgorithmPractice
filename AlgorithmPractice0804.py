import copy
import copyreg
from collections import deque

n, m = map(int, input().split(' '))
real_graph = [list(map(int, input().split(' '))) for _ in range(n)]
print(real_graph)
# 상 하 좌 우
d_col = [0, 0, -1, 1]
d_row = [-1, 1, 0, 0]

def virus_bfs(real_graph):
    queue = deque()
    graph = copy.deepcopy(real_graph)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        current_node = queue.popleft()
        for i in range(len(d_row)):
            next_row = d_row[i] + current_node[0]
            next_col = d_col[i] + current_node[1]
            if graph[next_row][next_col] == 2 or graph[next_row][next_col] == 1:
                continue
            if next_row < 0 or next_col < 0 or next_row > n or next_col > n:
                continue
            next_node = [next_row, next_col]
            graph[next_row][next_col] = 2
            queue.append(next_node)

    global answer
    cnt = 0

    for c in range(n):
        cnt += graph[c].count(0)

    answer = max(answer, cnt)

def build_wall(wall_cnt):
    if wall_cnt == 3:
        virus_bfs(real_graph)
    for i in range(n):
        for j in range(m):
            if real_graph[i][j] == 0:
                real_graph[i][j] = 1
                build_wall(wall_cnt+1)
                real_graph[i][j] = 0

answer = 0
build_wall(0)
print(answer)








# 1과 2가 아닌곳에 벽을 세운다
# 바이러스를 퍼트린다
# 안전구역을 세보고 최대의 안전구역 개수를 구한다.
