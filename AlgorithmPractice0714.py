import sys
from collections import deque

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[b].append(a)

def bfs(graph, start_node):
    node_count = 0
    queue = deque()
    visited = [[False] for _ in range(n + 1)]
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if visited[next_node] == True:
                continue
            queue.append(next_node)
            visited[next_node] = True
            node_count += 1
    return node_count

result = []
max_value = 0

for i in range(1, n+1):
    c = bfs(graph, i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
for e in result:
    print(e, end=' ')






