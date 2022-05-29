# 변수 = 최대값, 바로 직전값, 반복횟수, 반복 끝나는 조건문

# 5 8 4
# 2 4 5 4 6
# 46

# 6665666
# 5545545
n, m, k = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

numbers.sort(reverse=True)

count = 0
numbers_sum = 0
while True: # while True 쓰면 반복문 끝나는 조건문 꼭 써야해!!! 아님 무한루프 돌아
    if count >= m: # m 번 보다 크면 반복문 종료
        break
    max_num = numbers[0]
    numbers_sum += max_num * k
    second_max_num = numbers[1] # 6665 이걸 한묶음으로 더해주는걸 반복
    numbers_sum += second_max_num #여기까지 더하면 k+1번 더한것
    count += (k+1) # count = 반복횟수
    #그리고 언제 반복문을 멈춰야되는지 생각하고 while조건문 밑에다가 적어

# while 조건문 빠져나왔는데 이미 m번 이상 더해져있을때 어떻게 할지 조건문 있어야겟지!
# 그럼 m번보다 더 더했으면 더 더한만큼 빼주면 돼!
if count > m:  #만약 m이 8인데 10번 count됐으면 10(count) - 8(m) 하면 초과로 더해진 2번이 나옴
    # # 만약 66566566, 666566 이 정답인 배열이라면 665 6665가 한묶음이라서 초과로 더해진게 하나라면 두번째로 큰수 일수밖에 없음
    # 666566656
    if count - m == 1:
        print(numbers_sum - numbers[1])
    else:
        print(numbers_sum - numbers[1] - numbers[0] * (count - m - 1))
else:
    print(numbers_sum)

# 구현

# 문제 - 2
# 첫번째 방법
n = int(input())
route = input().split()

# (1,1)
# RRRUDD
current_coord = [1,1] #튜플()은 내부값을 변경할 수 없기때문에 리스트 형태로 쓴다.
for i in range(len(route)):
    direction = route[i]
    if direction == 'R':
        if current_coord[1] == n: #오른쪽으로 갈때는 정해진 범위에서 벗어나면 무시
            continue
        current_coord[1] += 1
    elif direction == 'L':
        if current_coord[1] == 1: #만약 이미 current_coord가 [1,1]이면 왼쪽으로 갈시 범위를 벗어나므로 무시
            continue
        current_coord[1] -= 1
    elif direction == 'U':
        if current_coord[0] == 1: #위로 갈때 좌표가 0이 되면 지도에서 벗어나므로 무시
            continue
        current_coord[0] -= 1
    elif direction == 'D':
        if current_coord[0] == n:
            continue
        current_coord[0] += 1
    #print(direction, current_coord)

#print(current_coord[0], current_coord[1])

# 두번째 방법 - 더 깔끔한 방법
n = int(input())
route = input().split(" ")

# L R U D
d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]
moves = ["L", "R", "U", "D"]

current_coord = [1, 1]
for i in range(len(route)):
    direction = route[i] # # route는 RRRDDD 이런 리스트니깐 하나씩 꺼내자. direction이라는 변수에 담는다.
    index = moves.index(direction) # list.index(인자)는 인자가 몇번째 인덱스인지 찾아준다. "R"이 direction에 담아졌으면 "R"를 moves랑 매치시켜서 인덱스번호 반환
    next_row = current_coord[0] + d_row[index] # current_coord[0] 이 행
    next_col = current_coord[1] + d_col[index] # 다음 좌표는 현재 좌표에다가 row/col 를 더한값
    if next_row < 1 or next_row > n or next_col < 0 or next_col > n: # 예외처리 : 범위를 벗어나면 무시하는 조건문
        continue
    # 범위를 안 벗어난다면 교체
    current_coord[0] = next_row
    current_coord[1] = next_col

#print(current_coord[0], current_coord[1])


# 문제 - 3
# 상하좌우를 순회하면서 0인지 확인해야돼 = dfs, bfs

# graph의 표현방식 = 인접행렬 / 연결 리스트
# 00110
# 00011
# 11111
# 00000

# n = 행, m = 열
n, m = map(int, input().split(' '))
graph = [list(map(int, input())) for _ in range(n)]
print(graph)
from collections import deque
visited = [[False] * m for _ in range(n)]
print(graph)
print(visited)

# L R U D
d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]

def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node[0]][start_node[1]] = True
    while queue:
        current_node = queue.popleft() # graph에서 0인 애들이 있어서 함수를 호출했으니깐 큐에서 빠진애들을 1로 바꿔준다.
        graph[current_node[0]][current_node[1]] = 1
        for i in range(len(d_row)): # 이제 주위에 0이 있는지 행 개수만큼 돌아
            #다음 좌표를 정의해주자
            next_row = current_node[0] + d_row[i]
            next_col = current_node[1] + d_col[i]
            if next_row < 0 or next_col < 0 or next_row > n - 1 or next_col > m - 1: # 갈수있는 범위인지 체크
                continue
            if visited[next_row][next_col]: # 그 좌표가 이미 방문처리되었으면
                continue
            if graph[next_row][next_col] == 1: #graph에서 좌표로 가봤는데 1이면
                continue
            queue.append([next_row, next_col]) # 좌표를 넣으면 됨
            visited[next_row][next_col] = True

# 0인지 확인하기 위해 2차원 배열 한번씩 돌기(이중 반복문)
count = 0
for row in range(n):
    for col in range(m):
        #이중문 돌면서 언제 일때 방문해야돼? 0일때!
        if graph[row][col] == 0: # graph의 좌표 graph[row][col] 이 0일때
            # bfs 순회돌면서 주위에 0있는지 찾아
            bfs(graph, visited, [row, col]) # 다 돌았어? 모여있는 0이 몇개인지 세!
            count += 1

print(count)

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

# n개의 숫자중에서 3장을 뽑아 합이 m을 넘지않는 최대의 합을

# 풀이 1

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

# 풀이 2

# n개의 숫자중에서 3장을 뽑아 합이 m을 넘지않는 최대의 합을 구해라

from itertools import combinations
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))
numbers = list(combinations(data, 3)) #numbers에는 카드 3장의 합이 들어있음
temp_list = []
for i in range(len(numbers)):
    if sum(numbers[i]) < m: #합이 m을 넘지 않고
        temp_list.append(sum(numbers[i]))
print(max(temp_list))


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

# 문제 1

n,m = list(map(int, input().split(' ')))
cards = [list(map(int, input())) for _ in range(n)]

max_value = 0
for i in range(n):
    min_row = min(cards[i]) # 각 행을 돌면서 리스트에서 최소값끼리 비교해서 큰 수를 찾는다
    if min_row > max_value:
        max_value = min_row
print(max_value)

# 문제 2
location = input()
location = [int(location[1]), ord(location[0])-96]


d_col = [-2, -2, 2, 2, -1, -1, 1, 1]
d_row = [-1, 1, -1, 1, 2, -2, -2, 2]
count = 0

for i in range(len(d_row)):
    next_row = location[0] + d_row[i]
    next_col = location[1] + d_col[i]
    if next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8:
        continue
    count += 1
print(count)


# 문제 4

n, k = list(map(int, input().split(' ')))
count = 0
if n < k:
    print('n이 커야합니다')
while True:
    if n == 1:
        break
    elif n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

# 문제 5
coin_list = [500, 100, 50, 10]
coin_num = 0
n = int(input())
if n % 10 != 0:
    print('10의 배수가 아닙니다')
else:
    for coin in coin_list:
        coin_num += int(n / coin)
        n %= coin
print(coin_num)

# 문제 - 1

# 문자열 S가 주어졌을때, SHA-256 해시값을 구하는 프로그램을 작성하시오
# 문제 풀이 핵심 아이디어
# 1. hashlib의 sha256 함수를 이용하면 SHA 256 해시를 구할수 있다.
# 2. hashlib.sha256(문자열의 바이트 객체).hexdigest() : 해시 결과 문자열

import hashlib
input_data = input()
encoded_data = input_data.encode() # 입력받은 객체의 바이트객체를 구하기위해서 encode() 함수를 불러오고
result = hashlib.sha256(encoded_data).hexdigest() #인코드가 된 데이터를 hashlib.sha256 함수안에 넣게되면 하나의 해시 객체가 만들어지고 hexidgest()함수를 불러온다
print(result)

# 문제 2
# 백준 1920
# # N개의 정수 A[1], A[2], ... A[N] 이 주어져 있을때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오

n = int(input())
a = list(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))

for i in range(n):
    if b[i] in a:
        print('1')
    else:
        print('0')

# 수업 코드
if i in b:
    if i not in a:
        print('0')
    else:
        print('1')

# 문제 3
# 백준 4195번

# 친구관계가 생길때마다 두사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오

# 문제 풀이 핵심 아이디어
# 1. 해시를 활용한 union-find(합집합 찾기) 알고리즘을 이용해 문제를 풀 수 있다.
# 2. python 에서는 dicitionary 자료형을 해시처럼 사용할 수 있다.

# 합집합 찾기(union-find) 알고리즘 코드
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]  # x네트워크의 크기에 y 네트워크 크기값을 더해주는것




parent = [] # union-find함수를 이용하게 될때는 parent라는 리스트나 딕셔너리를 만든다.

for i in range(0,5):
    parent.append(i)

print(union(1, 4))
print(union(2, 4))
# # 1, 1, 3, 1 이 출력되는데 이걸 보고 1번,2번,4번 원소가 하나의 집합인걸 알수있다. {1,2,4}, {3}

for i in range(1, len(parent)):
    print(find(i), end = ' ')

# 네트워크 크기까지 출력하는 코드

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x]) # x가 가리키는 부모를 재귀적으로 찾아서 진짜 부모를 가져온다음에
        parent[x] = p # 이제 개를 자기자신의 부모로 삼은다음
        return parent[x] # 부모 값 반환

def union(x,y):

    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict() # 지금 예제같은경우는 각각의 노드가 문자열이기때문에 dictionary형태가 더 적절
    number = dict()

f = int(input())

for _ in range(f):
    x, y = input().split(' ')

    if x not in parent: #각각의 x,y가 parent값을 가지고잇지않다면
        parent[x] = x #입력받은 데이터를 parent값으로
        number[x] = 1 # 자기 자신만 존재하기때문에 네트워크 크기를 1로 설정
    if y not in parent:
        parent[y] = y
        number[y] = 1

    union(x, y) # 이제 x와 y를 이어준다.

    print(number[find(x)])

# 기본 정렬 알고리즘 강의 4~7

# 문제 1
# 백준 2750
# 숫자가 n개 입력되면 입력된 숫자를 오름차순으로 출력한다.

n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)

# 백준 10814
# 문제 2

# 나이와 이름을 입력하면 나이순으로 정렬되어 출력하게 한다. 첫째줄에는 사람수N, 두번쨰줄부터 N개의 회원 나이와 이름을 쓴다
# 문제 풀이 핵심 아이디어
# 1. (나이, 이름)의 정보를 입력 받은 뒤에 나이를 기준으로 정렬
# 2. 파이썬의 기본 정렬 라이브러리를 이용하면 된다.


n = int(input())
client_list = []
for _ in range(n):
    input_data = input().split(' ')
    client_list.append((int(input_data[0]), input_data[1]))

client_list = sorted(client_list, key=lambda x: x[0]) # x[0] 첫번째 인덱스를 기준으로 삼도록 key 속성에 넣어줌으로써 정렬
for i in client_list:
    print(i[0], i[1])

### key = lambda x:x[0] 오름차순으로 정렬
### 우선 입력받아 저장할 변수를 만들고 그 변수 안에서 나이와 이름을 나눈다
### 나이 이름을 받으면 a.append((int(input_data[0]), input_data[1]))

# 백준 11650
# 문제 3
# 첫째줄에 점의 개수, 둘째줄부터 N개의 x, y 위치가 한자리수자로 입력받는다. 출력값을 x, y 좌표가 증가하는 순서로 정렬해라

# 문제 풀이 핵심 아이디어
# 1. (x좌표, y좌표)를 입력 받은 뒤, x좌표, y좌표 순서대로 차례대로 오름차순 정렬합니다
# 2. 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬합니다
# 3. 따라서 단순히 기본 정렬 라이브러리를 이용하면 됩니다.(key속성 설정 없이)

n = int(input())
array = []
for _ in range(n):
     coord = list(map(int, input().split(' ')))
     array.append(coord)

array.sort(reverse=True)
for i in array:
    print(i[0], i[1])

# array에는 리스트 형식으로 되어있어서 for i in array를 해서 하나씩 리스트에서 i[0] 첫번째 인덱스의 원소, 두번재 인덱스의 원소를 가져온다

# 문제 4
# 백준 2747

#계수 정렬 알고리즘 이용
# 인덱스 번호에 맞는 수가 들어오면 count를 해주는것
# 유의사항: 데이터의 개수가 많을때 파이썬에서는 sys.stdin.readline()를 사용해야한다.

import sys
n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1 # 입력받은 숫자와 같은 인덱스의 값을 증가시킨다

for i in range(10001): # 각 인덱스가 데이터의 범위가 되기떄문에
    if array[i] != 0: # 그 배열의 인덱스 값이 0이 아니라면 한번이라도 그 데이터가 나왔다라는 듯이니깐
        for j in range(array[i]): # 그 데이터가 나온 등장횟수만큼
            print(i) # 그 인덱스의값을 출력하도록 만든다


# 문제 5
# 실패코드

index = int(input())
fibo = [0 for _ in range(index + 1)]


def fibo(index):
    if index <= 1:
        return index
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, index + 1):
        fibo[index] = fibo[index - 2] + fibo[index - 1]
    return fibo[index]

# 이 문제에서 재귀함수를 사용하면 시간 초과를 일으킬수있다.

# 성공 코드

n = int(input())
a, b = 0, 1

while n>0:
    a, b = b, a + b # 더한값을 계속 덮어씌우는 식으로 작동

print(a)


# 백준 11004번
# 수 N개 A1, A2, ... A_N이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 k번째 있는 수를 구하는 프로그램을 작성하시오

# 출력
# A를 정렬했을 때, 앞에서부터 k번째 있는 수를 출력한다.

# 문제 풀이 핵심 아이디어
# 데이터의 개수가 최대 5000000개 이므로 시간 복잡도 O(NlogN)의 정렬 알고리즘을 이용해야한다.
# 고급 정렬 알고리즘(병합 정렬, 퀵 정렬, 힙 정렬 등)을 이용하여 문제를 해결가능

def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = int(len(data)) // 2
    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])
    merged = []
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] < right[right_point]:
            left.append(left[left_point])
            left_point += 1
        else:
            right.append(right[right_point])
            right_point += 1

        while len(left) > left_point:
            merged.append(left[left_point])
            left_point += 1

        while len(right) > right_point:
            merged.append(right[right_point])
            right_point += 1

        return merged


n, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
merged = merge_sort(data)
print(merged[k - 1])# k번째 원소를 출력해야 하기때문에 k-1을 입력

# 백준 1543
# 어떤 단어가 총 몇 번 등장하는지 세려고 한다. 중복하여 세지않고 예를 들어 문서가 abababa이고 찾으려는 단어가 ababa라면 최대 2번 등장한다.
# 입력 =  ababababa, aba
# 출력 = 2

document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word): # 문서가 단어를 벗어나기전까지 반복
    if document[index: index+len(word)] == word: # 문서에서 보고있는 단어가 찾고자 하는 단어인 경우
        result += 1
        index += len(word)
    else:
        index += 1
        print(result)

# 백준 1569
# 새

n = int(input())
# n = 14
# count = 7
k = 0
count = 0
while n >= 0:
    k += 1
    if n == 0:
        break
    if k > n:
        k = 0
    else:
        n = n - k
        count += 1
print(count)

# 강의 코드

result = 0
k = 1
while n != 0:
    if k > n :
        k = 1
    n -= k
    k += 1
    result += 1
print(result)

# 1302
# 제일 많이 팔린 책 제목 출력 문제

n = int(input())
book_list = list(str(input()) for _ in range(n))
book_count = {book_list[i] : 0 for i in range(n)}
sort_list = list()
for i in range(n):
    for key in book_count:
        if book_list[i] == key:
            book_count[key] += 1

for i in book_count:
    count = max(book_count.values())
    if book_count[i] == count:
        sort_list.append(i)
        sort_list.sort()
print(sort_list[0])

# 힘들엇다...좀더 열심히 공부...
# 계속 풀어보자...


# 시계 문제

three_list = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

n = int(input())

count = 0

for i in range(n + 1):
    if i in three_list:
        count += 1
    print('i',i)
    for m in range(60):
        if m in three_list:
            count += 1
        print('m',m)
        for s in range(60):
            if s in three_list:
                count += 1
            print('{0}시,{1}분,{2}초'.format(i,m,s))


print(count)




# 문제 6
# 백준 1439


# 알파벳 대문자 + 숫자

n = list(input())
alphabet= []
integer = []
count = 0
for i in range(len(n)):
    if 65 <= ord(n[i]) <= 90:
        alphabet.append(str(n[i]))
    else:
        integer.append(int(n[i]))
        count = sum(integer)

alphabet.sort()
string = ''.join(alphabet)
print('%s%d' % (string, count))


# 백준 18406 럭키스트라이크

n = list(str(input()))

if len(n) % 2 == 1:
    print('짝수 자릿수여야 합니다.')

medium = len(n) // 2
front = n[:medium]
back = n[medium:]
front_sum, back_sum = 0, 0

for i, j in zip(front, back):
    front_sum += int(i)
    back_sum += int(j)

if front_sum == back_sum:
    print('LUCKY')
else:
    print('READY')



# 문제9

n = list(map(int, input()))
count_one, count_zero = 0, 0
# i = 5, len(n) = 6

for j in range(len(n) - 1):
    if j+1 == len(n)-1: # 마지막 인덱스일때
        if n[j+1] == 1:
            count_one += 1
        else:
            count_zero += 1
    if n[j] != n[j + 1]:
        if n[j] == 1:
            count_one += 1
        else:
            count_zero += 1
    else:
        continue

print(count_one, count_zero)
if count_one <= count_zero :
    print(count_one)
else:
    print(count_zero)

# 공포도

n = int(input())
fear_list = list(map(int, input().split(' ')))
count_list = []

# 똑같은 수x를 세고 그 수가 x개 보다 많으면 최대값으로 설정
# 만약 최대값으로 설정한값보다 큰게 있으면 업데이트
count = 0
max_value = 0
for i in range(len(fear_list)):
    if fear_list[i] == fear_list[len(fear_list)-1]:
        count += 1
    count_list.append([fear_list[i],count])

max_count_list = []
for i in range(len(count_list)):
    if count_list[i][0] <= count_list[i][1]:
        max_count_list.append(count_list[i][1] - 1)
        for j in range(len(max_count_list)):
            if max_value < max_count_list[j]:
                max_value = max_count_list[j]
print(max_value)

# 문자열 연산 최대값 구하가ㅣ

n = list(map(int, input()))
result = n[0]

for i in range(1, len(n)):
    if n[i] == 0:
        continue
    elif result + n[i] > result * n[i]:
        result += n[i]

    else:
        result *= n[i]

print(result)

# 문제
# 정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.

n = int(input())


def make_two_digit(n):
    n = str(n)
    if len(n) == 2:  # 두자리면 두자리로 return
        return n
    else:  # 숫자 한자리라면 01, 02, 03 이렇게 앞에 0을 붙여 두자리 수로 바꿔준다.
        return '0' + n  # 단순하게 이렇게 문자'0'를 추가하면 됨


result = ''  # 빈 문자열
count = 0
for hour in range(0, n + 1):
    result += make_two_digit(hour)
    for minute in range(0, 60):
        result += make_two_digit(minute)
        for second in range(0, 60):
            result += make_two_digit(second)
            print(result)
            if '3' in result:
                count += 1
            result = result[0:4]  # second 반복문이 끝나면 슬라이싱해서 초기화해준다
        result = result[0:2]  # minute 반복문도 끝나면 시간(hour)만 나누고 싹 다 자르고서 새로운 분을 추가하는거다.
    result = ''  # 분도 끝났으면 시간을 바꿔야하니깐  새로운 시간으로 시작한다고 빈 문자열을 만든다.
print(count)

# 게임개발 문제

n, m = map(int, input().split(' '))
x, y, direction = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 무조건 input 받은거 출력부터 해서 체크 먼저 하기
print(n, m, x, y, direction)
print(graph)
print(visited)

# 북 서 남 동
# 0  1  2  3

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]


def re_index(index):
    while True:
        if index < 0:
            index += 4
        else: # 양수이면 반환해야지!
            return index


def dfs(graph, visited, current_node, direction):
    visited[current_node[0]][current_node[1]] = True
    direction = re_index(direction)
    direction -= 1

    for i in range(4):
        next_row = current_node[0] + d_row[direction]
        next_col = current_node[1] + d_col[direction]
        if next_row < 0 or next_col < 0 or next_row > n - 1 or next_col > m - 1:
            direction -= 1
            continue
        if visited[next_row][next_col] == True:
            direction -= 1
            continue
        if graph[next_row][next_col] == 1:
            direction -= 1
            continue
        next_node = [next_row, next_col]
        dfs(graph, visited, next_node, direction)
dfs(graph, visited, [x, y], direction)
answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            answer += 1
print(answer)

#백준 18352
# 최단거리 구하기

import heapq
import sys

n, m, k, start_node = list(map(int, sys.stdin.readline().split()))
graph = [None]
graph += [[] for _ in range(n)]
visited = [None]
visited += [-1] * n
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)


INF = 1e9
min_distance = [INF] * (n+1)

def dijkstra(graph, visited, start_node):
    queue = []
    heapq.heappush(queue, [0,start_node])
    visited[start_node] = 0
    while queue:
        [dist, current_node] = heapq.heappop(queue)
        for next_node in graph[current_node]:
            if visited[next_node] != -1:
                if visited[next_node] <= dist + 1:
                    continue
            heapq.heappush(queue, [dist+1, next_node])
            visited[next_node] = dist+ 1

dijkstra(graph, visited, start_node)
print(visited)
if k in visited:
    print(visited.index(k))
else:
    print(-1)


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



