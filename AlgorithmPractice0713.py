# 백준 2606

from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if visited[next_node] == True:
                continue
            queue.append(next_node)
            visited[next_node] = True


bfs(graph, visited, 1)
print(visited)
count = 0
for i in range(len(visited)):
    if visited[i] == True:
        count += 1
print(count-1)


# 백준 1012 유기농배추

from collections import deque

# 오른쪽 위쪽 왼쪽 아래쪽
d_row = [0, -1, 0, +1]
d_col = [+1, 0, -1, 0]

def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node[0]][start_node[1]] = True
    while queue:
        current_node = queue.popleft()
        for i in range(len(d_row)):
            next_row = current_node[0] + d_row[i]
            next_col = current_node[1] + d_col[i]
            if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > m-1:
                continue
            if visited[next_row][next_col] == True:
                continue
            if graph[next_row][next_col] == 0:
                continue
            next_node = [next_row, next_col]
            queue.append(next_node)
            visited[next_row][next_col] = True
            graph[next_row][next_col] = 0


t = int(input())

for _ in range(t):
    count = 0
    n, m, k = map(int, input().split(' '))
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split(' '))
        graph[a][b] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, visited, [i, j])
                count += 1

    print(count)
