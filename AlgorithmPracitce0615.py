import heapq
import sys

input = sys.stdin.readline


def dijkstra(start_node):
    queue = []
    heapq.heappush(queue, [0, start_node])
    min_distance[start_node] = 0
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if min_distance[current_node] < current_dist:
            continue
        for next_node in graph[current_node]:
            cost = current_dist + next_node[1]
            if min_distance[next_node[0]] < cost:
                continue
            min_distance[next_node[0]] = cost
            heapq.heappush(queue, [cost, next_node[0]])

t = int(input())
for _ in range(t):
    n, m, start_node = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    min_distance = [1e9] * (n + 1)
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph[b].append([a, cost])
    dijkstra(start_node)
    count = 0
    max_distance = 0
    for i in min_distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i  # 마지막노드까지의 거리는 제일 크니깐 거리값이 1e9아닌 노드중에서 제일 큰값을 찾는다. 그래서 들여쓰기 또한거
    print(count, max_distance)
