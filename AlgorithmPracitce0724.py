# n = int(input())
# score_list = list(map(int, input().split(' ')))
# max_num = max(score_list)
# min_num = min(score_list)
# result = max_num - min_num
# print(result)

# m = int(input())
# b_list = list(map(int, input().split(' ')))

# a_list = []
# for i in range(len(b_list)):
#     if i == 0:
#         a_list.append(b_list[i])
#     else:
#         temp = b_list[i] * (i+1)
#         result = temp - sum(a_list[:i])
#         a_list.append(result)
#
# for j in a_list:
#     print(j, end=' ')

# new_list = []
# alpha_list = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
# name = (input().split(' '))
# boy, girl = name[0], name[1]
# left_point, right_point = 0, 0
# merged = []
# while len(boy) > left_point or len(girl) > right_point:
#     if len(boy) > len(girl):
#         if right_point == len(girl):
#             merged.append(boy[left_point:])
#             break
#         merged.append(boy[left_point])
#         left_point += 1
#         merged.append(girl[right_point])
#         right_point += 1
#
#     elif len(boy) == len(girl):
#         merged.append(boy[left_point])
#         left_point += 1
#         merged.append(girl[right_point])
#         right_point += 1
#     else:
#         if left_point == len(boy):
#             merged.append(girl[right_point:])
#             break
#         merged.append(boy[left_point])
#         left_point += 1
#         merged.append(girl[right_point])
#         right_point += 1
#
# word = ''.join(merged)
#
# number_list = []
# import string
#
# pair_list = []
# for pair in zip(string.ascii_uppercase, alpha_list):
#     pair_list.append(pair)
#
# while True:
#     index = 0
#     for i in range(len(pair_list)):
#         if word[index] == pair_list[i][0]:
#             number_list.append(pair_list[i][1])
#             index += 1
# print(number_list)


# n = int(input())
# sheet = list(input())
# score = 0
# bonus = 0
# for i in range(len(sheet)):
#     if sheet[i] == "O":
#         score += i+1
#         if bonus >= 1:
#             score += bonus
#         bonus += 1
#     else:
#         bonus = 0
#
# print(score)

a, b = map(int, input().split(' '))
girl_group = []
for _ in range(a):
    group_name = str(input())
    group_number = int(input())
    for _ in range(group_number):
        girl_group.append([group_name, str(input())])

for _ in range(b):
    name = str(input())
    is_group = int(input())
    if is_group == 0:
        for i in range(len(girl_group)):
            if name == girl_group[i][0]:
                print(girl_group[i][1])
    else:
        for i in range(len(girl_group)):
            if name == girl_group[i][1]:
                print(girl_group[i][0])







