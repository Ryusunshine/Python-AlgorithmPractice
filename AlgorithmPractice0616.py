# 백준 3190 뱀
from copy import deepcopy

n = int(input())
graph = [[0] * n for _ in range(n)]


k = int(input())
for _ in range(k):
    [row, col] = list(map(int, input().split()))
    graph[row][col] = -1 # 사과있는곳을 -1로 둔다


snake = [[0, 0]]
snake_dir = "R"
end_game = False
end_time = 0

def get_next_coord(direction, current_coord):
    next_coord = deepcopy(current_coord)
    if direction == "R":
        next_coord[1] += 1
    elif direction == "L":
        next_coord[1] -= 1
    elif direction == "U":
        next_coord[0] -= 1
    else:
        next_coord[0] += 1
    return next_coord

def change_direction(current_dir, rotation):
    if current_dir == "L": #현재 방향이 L 왼쪽인데
        if rotation == "D": # D 오른쪽으로 꺾어야하면 위쪽임
            return "U"
        else: # 왼쪽으로 꺾어야하면 아래임
            return "D"
    elif current_dir == "R": #현재 방향이 오른쪽인데
        if rotation == "D": # D 오른쪽으로 꺾어야하면 아래
            return "D"
        else: # 왼쪽으로 꺾어야하면 위
            return "U"
    elif current_dir == "U": #현재 방향이 L 왼쪽인데
        if rotation == "D": # D 오른쪽으로 꺾어야하면 위쪽임
            return "R"
        else: # 왼쪽으로 꺾어야하면 아래임
            return "L"
    elif current_dir == "D": #현재 방향이 L 왼쪽인데
        if rotation == "D": # D 오른쪽으로 꺾어야하면 위쪽임
            return "L"
        else: # 왼쪽으로 꺾어야하면 아래임
            return "R"

start_time = 1
l = int(input())
for kkk in range(l):
    # D: 오른쪽 L : 왼쪽
    # 3 D
    [time, rotation]= input().split(" ")
    time = int(time)
    for t in range(start_time, time +1):# t초동안 R방향으로 간다
        if end_game == True:
            break
        head_coord = snake[len(snake) -1] # 머리좌표
        next_coord = get_next_coord(snake_dir, head_coord) #머리를 이동해야하기때문에 방향에 따라 머리좌표를 움직인다
        if 0 > next_coord[0] or 0 > next_coord[1] or next_coord[0] > n - 1 or next_coord[1] > n - 1:
            end_game = True
            break
        if next_coord in snake:#다음에 가려고하는 위치가 snake 배열안에 들어있어도 out
            end_game = True
            end_time = t
            break
        if graph[next_coord[0]][next_coord[1]] == -1:  # 좌표에 사과가 있는지 체크
            snake.append(next_coord)  # 뱀(리스트)에다가 다음 위치좌표를 더해주고 꼬리는 떼준다.
        else:
            snake.append(next_coord)
            del snake[0]

    snake_dir = change_direction(snake_dir, rotation)
    start_time += (time + 1 - start_time)
    print(start_time, kkk, l)
print(end_time)

