# 문제
# 정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.

n = int(input())


def make_two_digit(n):
    n = str(n)
    if len(n) == 2:  # 두자리면 두자리로 return
        return n
    else:  # 숫자 한자리라면 01, 02, 03 이렇게 앞에 0을 붙여 두자리 수로 바꿔준다.
        return '0' + n  # 단순하게 이렇게 문자'0'를 추가하면 됨


result = ''  # 빈 문자열
count = 0
for hour in range(0, n + 1):
    result += make_two_digit(hour)
    for minute in range(0, 60):
        result += make_two_digit(minute)
        for second in range(0, 60):
            result += make_two_digit(second)
            print(result)
            if '3' in result:
                count += 1
            result = result[0:4]  # second 반복문이 끝나면 슬라이싱해서 초기화해준다
        result = result[0:2]  # minute 반복문도 끝나면 시간(hour)만 나누고 싹 다 자르고서 새로운 분을 추가하는거다.
    result = ''  # 분도 끝났으면 시간을 바꿔야하니깐  새로운 시간으로 시작한다고 빈 문자열을 만든다.
print(count)

# 게임개발 문제

n, m = map(int, input().split(' '))
x, y, direction = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 무조건 input 받은거 출력부터 해서 체크 먼저 하기
print(n, m, x, y, direction)
print(graph)
print(visited)

# 북 서 남 동
# 0  1  2  3

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]


def re_index(index):
    while True:
        if index < 0:
            index += 4
        else: # 양수이면 반환해야지!
            return index


def dfs(graph, visited, current_node, direction):
    visited[current_node[0]][current_node[1]] = True
    direction = re_index(direction)
    direction -= 1

    for i in range(4):
        next_row = current_node[0] + d_row[direction]
        next_col = current_node[1] + d_col[direction]
        if next_row < 0 or next_col < 0 or next_row > n - 1 or next_col > m - 1:
            direction -= 1
            continue
        if visited[next_row][next_col] == True:
            direction -= 1
            continue
        if graph[next_row][next_col] == 1:
            direction -= 1
            continue
        next_node = [next_row, next_col]
        dfs(graph, visited, next_node, direction)
dfs(graph, visited, [x, y], direction)
answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            answer += 1
print(answer)

#백준 18352
# 최단거리 구하기

import heapq
import sys

n, m, k, start_node = list(map(int, sys.stdin.readline().split()))
graph = [None]
graph += [[] for _ in range(n)]
visited = [None]
visited += [-1] * n
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)


INF = 1e9
min_distance = [INF] * (n+1)

def dijkstra(graph, visited, start_node):
    queue = []
    heapq.heappush(queue, [0,start_node])
    visited[start_node] = 0
    while queue:
        [dist, current_node] = heapq.heappop(queue)
        for next_node in graph[current_node]:
            if visited[next_node] != -1:
                if visited[next_node] <= dist + 1:
                    continue
            heapq.heappush(queue, [dist+1, next_node])
            visited[next_node] = dist+ 1

dijkstra(graph, visited, start_node)
print(visited)
if k in visited:
    print(visited.index(k))
else:
    print(-1)