
# 백준 2606 바이러스문제

from collections import deque
m = int(input())
n = int(input())
graph = [[] for _ in range(m+1)]
visited = [False] * (m+1)

for _ in range(n):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

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
count = sum(visited) - 1
print(count)

# 백준 1697 바이러스
# 계속 반복해서 공부

from collections import deque

n, k = map(int, input().split())
MAX = 10001
result = [0] * MAX  #result는 걸린 시간 담는 리스트

def bfs(n, k):
    q = deque()
    q.append(n)
    while q:
        current_num = q.popleft()
        if current_num == k:
            return result[current_num]
        for next_num in (current_num+1, current_num-1, current_num*2):
            if 0 <= next_num < MAX and not result[next_num]:
                result[next_num] = result[current_num] + 1
                #result[next_num] 은 현재 정점, +1 은 이전정점에서 다음 정점까지 걸린 시간
                q.append(next_num)

# current_num = 이전 정점
# next_num = 다음정점
print(bfs(n, k))

# 백준 1012 배추
# bfs 문제

from collections import deque
d_row = [0, 0, -1, +1] # 오른쪽 왼쪽 위 아래
d_col = [+1, -1, 0, 0]

def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node[0]][start_node[1]] = True
    while queue:
        current_node = queue.popleft()
        graph[current_node[0]][current_node[1]] = 0
        for i in range(len(d_row)):
            next_row = current_node[0] + d_row[i]
            next_col = current_node[1] + d_col[i]
            if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > m-1:
                continue
            if visited[next_row][next_col] == True:
                continue
            if graph[next_row][next_col] == 0:
                continue
            queue.append([next_row, next_col])
            visited[next_row][next_col] = True


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    visited = [[False] * (m) for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, visited, [i, j])
                count += 1
    print(count)







# 먼저 너가 문제를 미리 풀고 어떻게 푸는지 컴퓨터에 알려주는거야