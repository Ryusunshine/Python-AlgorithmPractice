# 프로그래머스 42891
# 무지의 먹방

# 1 2 3: 이미 그 금액의 동전이 있거나
# 4 = 2 + 1 + 1: 그 금액보다 작은 동전의 합

# 1. 내가 다 해봣어ㄷㄷ 진찌 안됨 => 완전탐색 -> for/ 재귀(dfs) / 큐(bfs, 다익스트라) / 다이나믹
# 2.  특정 조건을 따져서 해결 => 그리디

from itertools import combinations


def get_all_sums(coins, total_sum):
    for cnt in range(2, len(coins) + 1):
        results = combinations(coins, cnt)
        for result in results:  # 근데 우리는 중간에 한번이라도 원하는 합이 나오면 반복문 그만하길 원함
            if sum(result) == total_sum:
                return True
    return False


n = int(input())
coins = list(map(int, input().split()))
coins.sort()
coin_sum = sum(coins)
for total_sum in range(1, coin_sum + 1):
    if total_sum in coins:
        continue
    temp_list = []
    for coin in coins:
        if coin < total_sum:
            temp_list.append(coin)
        else:
            break
    if get_all_sums(coins, total_sum) == True:
        continue
    print(total_sum)  # 만약 False이면 가지고 있는 동전으로 합이 안나온다는뜻
    break
