# 알고리즘 강의 다시 듣고 다시 풀기
# 복습
# 백준 2798 카지노

from itertools import combinations

n, m = map(int, input().split(' '))
cards_num = list(map(int, input().split(' ')))
random_cards_list = list(combinations(cards_num, 3))
m_under_sum = []
for i in random_cards_list:
    cards_sum = sum(i)
    if cards_sum <= m:
        m_under_sum.append(cards_sum)
print(max(m_under_sum))


graph = [["1"],
         ["+2", "-2", "*2"],
         ["+3", "-3", "*3"]]


def dfs(graph, current_node, result, answer):
    result += (graph[current_node[0]][current_node[1]]) # 행, 열 좌표
    if current_node[0] == len(graph) - 1: # 마지막 행이면
        temp = result
        print('result', result)
        while True:
            if " " in temp:
                temp = temp.replace(" ", "")
            else:
                break
        print(result, eval(temp))
        return

# eval("1+2") 라는 문자열이 매개변수로 들어오면출력 값으로 3이라는 값을 반환

    for i in range(3):
        next_node = [current_node[0] + 1, i] #다음행(current_node[0] + 1) , 모든 열(i)
        dfs(graph, next_node, result, answer)


answer = []
dfs(graph, [0, 0], "", answer)