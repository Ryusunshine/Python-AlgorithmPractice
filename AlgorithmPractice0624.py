# 수업 - 알고리즘 유형별 문제풀이
# 강사 - 나동빈
# 기본 자료구조- 기초 문제 풀이

# 문제 - 1
# 입력한 숫자가 오름차순인지 내림차순인지 판단하는 코드를 작성하시오.

# 내가 작성한 코드
numbers = list(map(int, input().split(' ')))
print(numbers)
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
if numbers == ascending:
    print('ascending')
elif numbers == descending:
    print('descending')
else:
    print('mixed')

# 수업 코드
a = list(map(int, input().split(' ')))
ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = True
    elif a[i] < a[i - 1]:
        ascending = True

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

## 외워!
# 1. sorted(리스트, reverse=True)
# 2. if, elif, else

# 문제 -2
# 백준 2798번 문제
# 배열, 완전 탐색

# n개의 숫자중에서 3장을 뽑아 합이 m을 넘지않는 최대의 합을 구해라

n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
count = 0
for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)): # 중복 안되게 할려면 인덱스번호를 i + 1, j+1 이런식으로 써야해!!
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value) # 반복문 돌면서 업데이트되는 sum 값과 result 비교
print(result)

# 외워
# result = max(result, sum_value)
# max(a,b) = a와 b중에 더 큰값을 출력

# 문제 -3
# 백준 1874번 문제
# 스택, 그리디

n = int(input())
number = 1
stack = []
result = []

for i in range(1, n+1): # 데이터 개수만큼 반복해서 입력받음
    data = int(input())
    while number <= data: # 입력 받은 데이터에 도달할때까지 삽입
        stack.append(number)
        number += 1 # 1,2,3,4...씩 입력받은 숫자에 도달할때까지 append 해주기
        result.append('+')
        if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을때 출력. 아니면 못뽑음
            stack.pop() # [-1] 안써도 stack이니깐 마지막으로 들어온 원소를 반환
            result.append('-')
        else: # 스택의 최상위 원소가 데이터와 같지않으면 못빼기때문에 불가능 출력
            print('No')
            exit(0)
print('\n'.join(result)) # 가능한 경우

# 문제 3
# 백준 1966 번
# 큐, 구현, 그리디

# 수업 코드
# 확인하고자하는 문서가 실질적으로 몇번째에 출력되는지가 문제에서 요구하는 내용

test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = ((i, idx) for idx, i in enumerate(queue))
# enumerate는 특정 리스트를 각각 인덱스랑 같이 저장.
# 즉 여기서는 인덱스를 튜플의 두번째 원소로 설정하여 저장(ex. [2,1,4,3] = (2,0), (1,1), (4, 2), (3,3)

count = 0
while True:
    if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
        # queue[0][0] = 튜플의 가장 먼저 원소의 첫번째 값(즉 중요도)가 현재 queue에서의 가장 큰 중요도와 동일하다면
        count += 1 # count 증가
        if queue[0][1] == m: # 그 뽑은 문서가 찾고자 하는 입력한 m과 동일하다면
            print(count) # 현재까지 몇번의 문서가 출력되었는지 출력
            break
        else: # m이 아니라면
            queue.pop(0) # 단순하게 해당 문서를 그냥 뽑으면 됨
    else:
        queue.append(queue.pop(0)) # 중요도가 가장 높은 문서가 아니라면 다시 뒤쪽에 보내기위해서 pop해서 append해준다

# enumerate는 특정 리스트를 각각 인덱스랑 같이 저장. 즉 여기서는 인덱스를 튜플의 두번째 원소로 설정하여 저장(ex. [2,1,4,3] = (2,0), (1,1), (4, 2), (3,3))

# sth = [(idx, i) for idx, i in enumerate arr]
    # 증가하는 인덱스를 같이 넣은 튜플을 원소로 하는 배열생성
    # 예를 들어 arr=[5,6,8,10]

# sth = max(arr, key=lambda x: x[0])[0]
    # 2차원 배열에서 열의 첫번째 값이 가장 큰 원소를 찾고,
    # 그 값의 1번째 값 리턴
    # 예시 arr = [[1,2,3],[4,5,6],[7,8,9]]
    # sth = max(arr, key=lambda x: x[0])[0]
    # sth = 7




