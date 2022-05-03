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
    if j+1 == len(n)-1:
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