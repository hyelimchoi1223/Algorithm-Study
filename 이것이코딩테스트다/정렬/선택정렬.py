item = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
current = 0
while current < len(item):
    min_value = min(item[current:])
    min_index = item.index(min_value)
    item[current], item[min_index] = (
        item[min_index],
        item[current],
    )
    print(item)
    current += 1
