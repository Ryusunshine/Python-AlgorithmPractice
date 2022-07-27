# 처음부터 차례대로 읽으면서 똑같은 알파벳이 뒤에 있나 체크해야돼
# 즉 한개씩 잘라서 생각할거냐 두개씩 잘라서 생각할거냐가 중요

#자르는 개수에 따라서 반복문을 돈다
# 자를 개수에 따라서 문자열의 처음부터 잘라서 배열을 만든다
# 같은 것의 개수를 세어서 압축한다 => [ab, ab, cd, cd] => [2ab, 2cd]
# 최소 길이의 압축 결과를 찾는다

# 내가 세운 계획을 한줄씩 클리어하면 문제 금방 풀수있다.

for cut_len in range(1, len(s)+1):
        print(cut_len)
        str_list = []
        i = 0
        while True:
            str_list.append(s[i:i+cut_len]) #단어의 길이만큼 자름

            i += cut_len
            if i + cut_len > len(s) - 1: #다음 자를 단어가 마지막 인덱스를 초과하지않았나 확인
                if s[i:len(s)] == " ": # 빈 문자가 아닌 경우를 체크
                    str_list.append(s[i:len(s)]) #break 하기전에 마지막 인덱스까지의 단어는 그냥 붙어줘야해. len(s)하면 len(s)직전까지 포함
                    break
                print(str_list)
                print()

 # 같은 문자열을 세어서 압축
 compressed_str_list = []
 start = str_list[0] # str_list[0]는 첫번째 원소
 cnt = 1
 for i in range(1, len(str_list)):
     if str_list[i] != start:
         compressed_str_list.append(f"{cnt}{start}" if cnt>1 else start) #반복되지 않으니 그냥 append. 그리고 다음 녀석도 이렇게 확인
         # 이렇게 start를 바꿔준다. 그리고 만약 cnt 가 1보다 크면 문자열 앞에 개수를 붙여줘야하고 {}안에 변수를 쓴다
         # 마지막 전의 우너소가 마지막 원소와 다르면 마지막 원소 그 자체도 append해줘야하므로 해당 조건문을 쓴다.
         if i == len(str_list) - 1:
             compressed_str_list.append(f"{str_list[i]}")
             start = str_list[i] # start가 초기화돼서 다시 반복문을 돈다
             cnt = 1 # count도 초기화
             #이번에는 뒤 문자열이 똑같은게 있으면 몇개인지 개수를 세야함
     else:

