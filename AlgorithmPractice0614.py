# 백준 1325
# 이 문제 계속 복습!!!!

# DFS: 1 -> 3 -> 4 -> 5
# DFS: 2 -> 3 -> 4 -> 5
# BFS는 못씀
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(graph, start_node):
    count = 1
    queue = deque()
    visited = [False] * (n + 1) # visited 무조건 함수 안에 들어와야해! 이것때문에 계속 오류 떳어
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if visited[next_node] == True:
                continue
            queue.append(next_node)
            visited[next_node] = True
            count += 1

    return count

result = []
max_value = 0

for i in range(1, n+1):
    answer = bfs(graph, i)
    print('모든 answer', answer)
    if max_value < answer:
        result = [i] # result = [], result.append(i)를 간소화한것
        print('result = [i]', [i])
        max_value = answer

    elif answer == max_value:
        print('elif answer', answer)
        result.append(i) # result = [1, 2]
        print(result)
        max_value = answer

for e in result:
    print(e, end=" ")
