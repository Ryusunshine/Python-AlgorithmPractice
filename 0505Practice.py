# 0001100
from collections import deque

n = list(str(input()))
visited = [False] * len(n)

def bfs(n):
    queue = deque()
    queue.append(n[0])
    while queue:
        current_element = queue.popleft()
        for i in range(1, len(n)):
            next_element = n[i + 1]
            if next_element != current_element:
                continue
            queue.append(next_element)


count_zero, count_one = 0, 0
for i in n:
    if i == 1:
        bfs(n)
        count_zero += 1
    else:
        bfs(n)
        count_one += 1

if count_zero > count_one:
    print(count_one)
else:
    print(count_zero)

    # 0001100

    n = list(str(input()))
    queue = list()


    def dfs(n, start_node):
        queue.append(start_node)
        while queue:
            current_node = queue.popleft()
            for i in n:
                next_node = current_node[i + 1]
                if next_node == current_node[i]:
                    queue.append(next_node)
                else:
                    continue


    for i in n:
        if i == 1:
            dfs(n, n[0])
            count_zero += 1
        else:
            dfs(n, n[0])
            count_one += 1

    if count_zero > count_one:
        print(count_one)


