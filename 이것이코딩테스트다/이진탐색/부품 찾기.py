N = int(input())
stocked_parts = list(map(int, input().split()))
M = int(input())
require = list(map(int, input().split()))

##### 내 풀이
# for r in require:
#     if r in stocked_parts:
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")


##### 이진 탐색 활용
def binary_search(items, target, start, end):
    if start > end:
        return None

    center = (start + end) // 2
    if items[center] == target:
        return center
    elif items[center] < target:
        return binary_search(items, target, center + 1, end)
    elif items[center] > target:
        return binary_search(items, target, start, center - 1)


stocked_parts = sorted(stocked_parts)

for r in require:
    result = binary_search(stocked_parts, r, 0, len(stocked_parts) - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
