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

