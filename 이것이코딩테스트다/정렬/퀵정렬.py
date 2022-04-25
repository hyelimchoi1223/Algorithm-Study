item = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def q_sort(item, start, end):
    if start >= end:
        return

    pivot_index = start
    left_index = start + 1
    right_index = end

    while True:
        while left_index <= end and item[left_index] <= item[pivot_index]:
            left_index += 1

        while right_index > start and item[right_index] >= item[pivot_index]:
            right_index -= 1

        if left_index > right_index:
            item[pivot_index], item[right_index] = (
                item[right_index],
                item[pivot_index],
            )
            pivot_index = right_index
            break
        else:
            item[right_index], item[left_index] = (
                item[left_index],
                item[right_index],
            )

    q_sort(item, start, pivot_index - 1)
    q_sort(item, pivot_index + 1, end)


q_sort(item, 0, len(item) - 1)
print(item)
