food_times = list(map(int, input().split(' ')))
k = int(input())

def re_index(index): # index = 5, food_times = 3 2
    if index >= len(food_times):
        index -= len(food_times)
    else:
        index
    return index

def solution(food_times, k):
    i = 0
    while k >= 0:
        i = re_index(i)
        if k == 0:
            print(i+1)
        if food_times[i] == 0:
            i += 1
        food_times[i] -= 1
        k -= 1
        i += 1

solution([3,1,2], 5)