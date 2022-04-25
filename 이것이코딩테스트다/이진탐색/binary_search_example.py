items = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

want_find = 4
start = 0
end = len(items) - 1
# center = end // 2

# while True:
#     if items[center] == want_find:
#         print(center)
#         break

#     if items[center] > want_find:
#         start = center + 1
#     elif items[center] < want_find:
#         end = center - 1

#     center = (end + start) // 2


def binary_search(array, target, start, end):
    if start > end:
        return

    center = (start + end) // 2
    if target == array[center]:
        return center
    elif array[center] > target:
        return binary_search(array, target, start, center - 1)
    elif array[center] < target:
        return binary_search(array, target, center + 1, end)


print(binary_search(items, want_find, start, end))
