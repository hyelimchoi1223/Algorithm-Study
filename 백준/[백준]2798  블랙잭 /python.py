from itertools import combinations

N, M = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))

max_num = 0
for x, y, z in combinations(numbers, 3):
    sum_result = x + y + z
    if sum_result > M:
        continue

    if max_num < sum_result:
        max_num = sum_result


print(max_num)
