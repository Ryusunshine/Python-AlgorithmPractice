

n= int(input())
height_list = list(int(input()) for _ in range(n))
left_count, right_count = 1, 1
# 0 1 2 3 4
left_max = height_list[0]
for i in range(1, n):
    if height_list[i] > left_max:
        left_max = height_list[i]
        left_count += 1

right_max = height_list[-1]
for j in range(n-1, 0, -1):
    if height_list[j] > right_max:
        right_max = height_list[j]
        right_count += 1

print(left_count)
print(right_count)


def ascending(list):
    smallest = height_list[0]
    count = 1
    for i in range(1, len(height_list)):
        if smallest < list[i]:
            count += 1
            smallest = height_list[i]
    return count


n = int(input())
for _ in range(n):
    height_list = list(int(input()) for _ in range(n))

print(ascending(height_list))
height_list.reverse()
print(ascending(height_list))





