#백준 18352
# 최단거리 구하기

import heapq

n, m, k, initial_node = list(map(int, input().split(' ')))
# n = 도시의 개수, m = 도로의 개수, k = 거리 정보, x = 출발 도시의 번호
graph = [list(map(int, input().split(' '))) for _ in range(m)]
# graph[i][0] = 출발노드, graph[i][1] = 도착노드

INF = 1e9
min_distance = [INF] * (n+1)


def dijkstra(graph, min_distance, initial_node):
    queue = []
    min_distance[initial_node] = 0
    heapq.heappush(queue, [min_distance[initial_node], initial_node])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if min_distance[current_node] < current_distance:
            continue
        for i in range(m):
            if graph[i][0] == current_node:
                next_node = graph[i][1]
                cost = current_distance + 1
                if cost < min_distance[next_node]:
                    min_distance[next_node] = cost
                    heapq.heappush(queue, [min_distance[next_node], next_node])


    return min_distance



for i in range(1, len(dijkstra(graph, min_distance, initial_node))):
    if dijkstra(graph, min_distance, initial_node)[i] == k:
        print(i)

    else:
        if k not in dijkstra(graph, min_distance, initial_node):
            print('-1')
            break





