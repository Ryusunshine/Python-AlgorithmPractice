# 문제의 요구사항은 정렬된 센서들을 최대 K개의 영역으로 나누는것과 동일
# k = 2이기 때문에 2개의 묶음으로 나눈다. 각 집중국의 수신 가능 영역은 다음과 같음
# 1~3(거리차이= 2), 6~9(거리차이= 3)
# 두개의 거리차이의 합 = 5
# 즉 수신 가능 영역의 길이의 합의 최솟값 = 5
#
# 문제의 알고리즘 풀이
# 각 센서를 오름차순으로 정렬
# 각 센서 사이의 거리를 계산

# 문제 푸는 방법
# 가장 거리가 먼 순서대로 제거. 즉  k-1개번 반복
# 1 - 3 = 2
# 6 - 6 - 7 - 9 = 0 - 1 - 2(거리차이)
# 그리고 남은 거리를 더하면 모든 집중국들의 영역의 합
# 남아있는 모든 거리들의 합 = 5

import sys
n = int(input())
k = int(input())

# 집중국의 개수가 n이상일때
if k >= n:
    print(0)
    sys.exit()

# 모든 센서의 위치를 입력받아 오름차순 정렬
array = list(map(int, input().split(' ')))
array.sort()

# 센서간 거리의 내림차 정렬
distances = []
for i in range(1, n):
    distances.append(array[i] - array[i -1] )
    distances.sort(reverse = True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k - 1):
    # 거리를 0 으로 만듦으로써 제거. 이걸 k -1 만큼 반복
    distances[i] = 0
print(sum(distances))


# 백준 1461 도서관
# 탐욕 알고리즘

# 음수와 양수에 대해여 개별적으로, m개씩 묶어서 처리

import heapq
# heapq는 음수도 인식하기때문에 가장 큰 마이너스값, 즉 가장 작은값을 구하기위해 모든 원소를 마이너스로 바꿔준다.

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
positive = []
negative = []

# 가장 거리가 먼 책의 위치찾기
farest = max(max(array), -min(array))

for i in array:
    # 책의 위치가 양수인 경우
    if i > 0:
        heapq.heappush(positive, -i)
    # 책의 위치가 음수인경우
    else:
        heapq.heappush(negative, i)

result = 0
while positive:
    # 한번에 m개씩 옮길수 있으므로 m개씩 빼낸다
    result += heapq.heappop(positive)
    for _ in range(m-1): # #나머지도 뽑는다
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m-1):
        heapq.heappop(negative)

#왕복거리를 계산해야되기때문에 *2 해주지만 가장 먼곳은 편도로 계산해야하니깐 한번 빼준다
print(-result * 2 - farest)
