n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]

# 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

#코테 문제 풀이 생각 순서
#1. 가능한 모든 벽 세우기를 다 해보고 그 중에서 안전구역이 최대인걸 고르자 = 완전 탐색 방법
# 	-> 혹시 시간 초과 또는 메모리 초과가 예상된다면? = 문제의 입력에 힌트가 있다.
#	-> 아래의 방법
#2. 도대체 벽을 어떻게 신박하게 세워야 안전구역이 최대가 되지? => 똑똑이 풀이법

#62 combination 3 = 60*60*60 / 6 = 36000 => 완전 탐색 충분
# 만약 1000만번이 넘어가는 시간 복잡도라면 아래의 방법을 고려하자

# 풀이방법
# 쉬운버젼
# 우선 벽을 3개를 세우는 모든 경우를 생각하자
# 그 중 하나의 경우에 대해서 벽을 세우고 => 바이러스를 퍼져 나가게 만들어보자(bfs) = > 안전구역을 계산해서 => 이게 최대인가 확인!

# 벽3개를 세우는 방법2(어려운 버젼)
# 완전 탐색 전략1: for문과 while문: 완전 탐색의 대상이 이미 다 주어진 경우
# 완전 탐색 전략2: DFS(for문과 재귀의 절묘한 조합 + 메모장) / BFS(큐의 푸쉬와 팝을 통한 절묘한 순서 + 메모장) : 완전 탐색의 대상을 직접 생성해야 하는 경우

# 완전 탐색 전략2 예제
# a, b, c => aaa, aab, aac, ..., ccc
# 인접리스트: [a, b, c],count

def dfs(graph, str_memo, current_node):
	str_memo += current_node
	if len(str_memo) == 3:
		print(str_memo)
		return
	next_nodes = ['a', 'b', 'c'] if len(str_memo) <= 2 else []
	for next_node in next_nodes:
		dfs(graph, str_memo, next_node)

dfs(['a', 'b', 'c'], '', 'a')
dfs(['a', 'b', 'c'], '', 'b')
dfs(['a', 'b', 'c'], '', 'c')

#str_memo += current_node 대신에 str_memo.append(current_node)로 적으면 에러나므로 str_memo += current_node로 적어야해!

# 완전탐색 전략 방법2
for first in ['a','b','c']:
	answer += first
	for second in ['a','b','c']:
		answer += second
		for third in ['a','b','c']:
			answer += third
			print(answer)
			answer = answer[:2]
		answer = answer[:1]
	answer = ' '

