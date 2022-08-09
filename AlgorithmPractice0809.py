# 이분탐색
# 1. 과연 이 문제를 완전탐색할수있는 문제인가
# = 내가 총 n개의 집에서 c개의 공유기 위치를 모두 고려해본다고 치자. 그중에서 최소거리를 찾는다.  n 콤비네이션으로 해야하지만 n범위가 20만개이기때문에 완전탐색 안됨.input의 범위를 보고 시간복잡도를 생각하고서 완전탐색 방법이 가능한지 파악해
#
# 2. 똑똑이 방법(이분탐색)
# 이분탐색 = 바이너리 서치
# 중간지점을 찾고 범위가 탐색범위가 아니면 재탐색을 해야하는데 중간지점을 제외한 나머지 절반 으로 옮기는 식으로 진행한다.
data = [1, 2, 3, 7, 8, 9]

# 방법1
def get_index(data):
    for i in range(len(data)):
        if data[i] ==7:
            print(i)
            break
print(get_index(data))
# O(n)의 시간이 걸림. 시간초과

# 방법2
def binary_search(start, end, target, result):
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    if data[mid] < target:
        return binary_search(data, mid + 1, end, target, result)
    elif data[mid] > target:
        return binary_search(data, start, mid - 1, target, result)


# 백준 2110 공유기 설치
# 출처: https://bgeun2.tistory.com/63

# 1.  집과 집 사이의 거리 최솟값 1을 start, 집과 집 사이의 거리 최댓값을 end로 초기화해준다.
#   (문제에서 집 여러 개가 같은 좌표를 가질 수 없다고 했으므로 최솟값은 1, 최댓값은 입력받은 집들의 좌표를 정렬한 후 0번 인덱스와 n-1번 인덱스와의 차이)
# 2. start와 end를 가지고 mid값을 구하고 해당 mid 값을 공유기 사이 거리의 최솟값으로 정했을 때 주어진 집 좌표에서 공유기를 총 몇 개 설치할 수 있는지 구한다.
# 3. 만약 공유기를 c개 보다 적게 설치 할 수 있다면 공유기 사이의 거리가 먼 것이기 때문에 end를 mid-1로 변경하여 사이의 거리 mid를 작게 해 준다.
# 4. 공유기를 c개 보다 많거나 같게 설치할 수 있다면 공유기 사이의 거리가 가까운 것이기 때문에 start를 mid + 1로 변경하여 거리 mid를 크게 해 주고,
#   리스트 'result'에 추가를 해준다.
# 5. 마지막으로 리스트 'result'에 저장된 수 중 가장 큰 값을 출력해준다.

import sys

n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]

house.sort()

# 공유기 사이 거리 최솟값
start = 1
# 공유기 사이 거리 최댓값
end = house[n - 1] - house[0]
result = []

while start <= end:
    count = 1
    mid = (start + end) // 2
    current = house[0]  # 공유기가 설치된 집의 위치
    for i in house:
        if current + mid <= i:  # 공유기 설치
            count += 1
            current = i
    if count >= c:  # mid 값에 따라 설치된 공유기의 개수가 c 보다 많거나 같으면
        start = mid + 1  # 거리를 늘린다.
        result.append(mid)
    else:
        end = mid - 1  # c 보다 작으면 거리를  줄인다.

print(max(result))

