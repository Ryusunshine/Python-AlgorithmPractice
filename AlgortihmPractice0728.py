import heapq
import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split(' '))
graph = [None]
graph += [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
INF = 1e9
min_dist = [INF] * (n+1)

def dfs(graph, min_dist, prev_node, current_node):
    # 현재 노드까지 이동거리 = 바로 직전에 있던 노드까지의 이동거리 + 1
 	# 새롭게 알게 된 현재 노드까지 이동거리가 메모장에 적혀있는 최단 이도거리보다 더 짧은가?
 	# 만약 그렇다면 값을 업데이트

    current_node_dist = min_dist[prev_node] + 1
    if current_node_dist < min_dist[current_node]:
        min_dist[current_node] = current_node_dist

    for next_node in graph[current_node]:
        dfs(graph, min_dist, current_node, next_node)

min_dist[x] = 0
dfs(graph, min_dist, x, x)

result = []
for i in range(len(min_dist)):
    if min_dist[i] == k:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for j in result:
        print(j, end = ' ')

# bfs로 풀어보기
# # bfs는 거품처럼 커지는 형태이기때문에 동시에 갈수있는 루트를 모두 한꺼번에 가보므로
# 한번 가본 노드를 또 다시 방문할 필요가 없다.

def bfs(graph, min_dist, start_node):
    queue = deque()
    queue.append(start_node)
    min_dist[start_node] = 0
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if min_dist[next_node] != INF:
                # INF이 아니면 한번이라도 방문해서 값을 갱신한것이기 때문에 INF이 아니면 지나치고
                # 방문한적이 없으면 값을 갱신해준다
                queue.append(current_node)
                min_dist[next_node] = min_dist[current_node] + 1