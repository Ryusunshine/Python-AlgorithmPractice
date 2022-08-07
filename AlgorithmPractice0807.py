# 백준 1753 최단경로

import heapq
import sys

input = sys.stdin.readline
INF = 1e9
x, y= map(int, input().split(' '))
graph = [[] for _ in range(x+1)]
min_distance = [None]
min_distance += [INF] * x

start_node = int(input())
for _ in range(y):
     u, v, w = map(int, input().split(' '))
     graph[u].append([v, w])

def dijkstra(graph, start_node, min_distance):
     queue = []
     heapq.heappush(queue, [0, start_node])
     min_distance[start_node] = 0
     while queue:
          current_dist, current_node = heapq.heappop(queue) # queue에는 거리랑 노드 정보 들어있음
          if min_distance[current_node] < current_dist:
               continue
          min_distance[current_node] = current_dist
          for next_node, weight in graph[current_node]: # graph는 next_node, weight 정보 들어있음
               cost = min_distance[current_node] + weight
               if cost < min_distance[next_node]:
                    min_distance[next_node] = cost
                    heapq.heappush(queue, [cost, next_node])

     return min_distance

dijkstra(graph, start_node, min_distance)
for i in range(1, len(min_distance)):
     if min_distance[i] == INF:
          print("INF")
     else:
          print(min_distance[i])







