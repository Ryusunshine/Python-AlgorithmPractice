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


parent[y] = x

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
