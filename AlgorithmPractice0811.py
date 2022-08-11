# 백준 1439 뒤집기
# 그리디

s = list(map(int, input()))
one_cnt, zero_cnt = 0, 0
print(len(s))
print(len(s)-1)
for i in range(1, len(s)):
    if i == len(s)-1:
        if s[i] == s[i-1]:
            if s[i] == 0:
                zero_cnt += 1
            else:
                one_cnt += 1

        else:
            one_cnt += 1
            zero_cnt += 1

    elif s[i] != s[i-1]:
        if s[i-1] == 0:
            zero_cnt += 1
        else:
            one_cnt += 1

    else:
        continue
print(min(zero_cnt, one_cnt))
