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







