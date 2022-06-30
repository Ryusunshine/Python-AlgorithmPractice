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