# 볼링공 무게 문제

n, m = map(int, input().split(' '))
weight_list = list(map(int, input().split(' ')))

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if weight_list[i] == weight_list[j]:
            count += 1
result = int((n * (n-1)) / 2) - count
print(result)

# 사과있는 칸이 1
# 1. 만약 사과가 있다면 (visited X) & next_node == 1:
# visited처리하고 그 칸이 0으로 바뀜.
# 2. 사과가 없다면 몸길이줄여서 꼬리가 위치한 칸을 비워준다. 즉 몸길이는 변하지 않는다.

# 입력

n = int(input())# 보드의 크기 n
k = int(input())# 사과의 개수 k
location = [list(map(int, input().split(' '))) for _ in range(k)] # 사과의 위치 x y 행 열
l = int(input()) # 뱀의 방향 변화 횟수 L
information = [list(input().split(' ')) for _ in range(l)] # 정수 x 문자 c
visited = [[False] * n for _ in range(n)]
snake = 1
current_node = [0,1]
# 동 서 남 북
# 0  1  2  3
d_row = [0, 0, 1, -1]
d_col = [1, -1, 0, 0]
def dfs(graph, visited, current_node, information):
    visited[current_node[0]][current_node[1]] = True
    direction = 0
    for i in range(l): #information 리스트에 저장되어있는 정보 순서대로 꺼내기
        next_row = current_node[0] + (d_row[direction] * information[i][0])
        next_col = current_node[1] + (d_col[direction] * information[i][0]) #이동
        second += information[i][0] # 몇초 지낫는지 더해주기
        if information[i][1] == 'D': # 이동은 한 상태, 회전 D= 오른쪽, L = 왼쪽
            direction -= 1
        else:
            direction += 1 # 회전도 해주고

        if next_row <= 0 or next_col >= 0 or next_row >= n - 1 or next_col >= n - 1:
                return second
        if visited[next_row][next_col] == True:
                continue
        current_node = [next_row, next_col]
        for j in range(len(location)):
            if location[j] == graph[next_row][next_col]: #다음 갈곳에 사과가 있다면
                visited[next_row][next_col] = True #방문처리해주고
            else:
                visited[next_row][next_col] = True
                snake -= 1







        next_row = current_node[0] + d_row[i]
        next_col =












