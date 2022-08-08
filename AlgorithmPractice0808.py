# 백준 11404
# 플로이드 알고리즴
# 가능한 모든쌍에 대해서 모든것을 다 구하는 알고리즘
# 플로이드 알고리즘은 인접행렬을 쓴다.
# 인접행렬은 두 도시가 있을때 두 도시사이의 거리를 즉각 답변할수있다.

n = int(input())
m = int(input())
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split(' '))
    graph[a][b] = c
    # c는 걸리는 시간인데 만약 c보다 더 작은값이 나오면 업데이트 해야한다
    graph[a][b] = min(c, graph[a][b])
for i in range(1, n+1):
    graph[i][i] = 0
    # 나 자신으로 가는 경로는 0으로 설정한다

# 알고리즘
#middle를 하나 고정해놓고 start랑 end를 바꿔가면서 더 작은거리로 가는 경로가 있으면 업데이트해준다.
#원래값보다 중간지점(middle)을 거쳐서 마지막 지점까지 거리의 합을 비교해서 더 작은것으로 업데이트한다.
for middle in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][middle]+ graph[middle][end])

# 정답
for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end = ' ')
    print() # 한줄 띄우기

