# 백준 17269 이름궁합

import sys
from string import ascii_uppercase

num_list = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
dic = dict(zip(ascii_uppercase, num_list))

input = sys.stdin.readline
n, m = map(int, input().split(' '))
name1, name2 = map(str, input().split(' '))

name3 = ''
min_len = min(n,m)
for i in range(min_len):
    name3 += name1[i] + name2[i]
name3 += name1[min_len:] + name2[min_len:]

lst = []
for i in name3:
    if i == '\n':
        continue
    lst.append(dic[i])

for i in range(n+m-2):
    tmp=[]
    for j in range(len(lst)-1):
        tmp.append((lst[j]+lst[j+1])%10)
    lst=tmp
print("{}%".format(lst[0]* 10 + lst[1]))

##################################################################################################################
# 백준 17389

n = int(input())
s = list(map(str, input()))

bonus = 0
total_sum = 0

for i in range(len(s)):
    if s[i] == "O":
        total_sum += i+1
        if bonus >= 1:
            total_sum += bonus
        bonus += 1

    else:
        bonus = 0

print(total_sum)

##################################################################################################################3

# 백준 16165 걸그룹 마스터 준석이

n, m = map(int, input().split(' '))

team_mem, mem_team = {}, {}
for i in range(n):
    team_name = input()
    mem_num = int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for j in range(m):
    name, num = input(), int(input())
    if num:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)