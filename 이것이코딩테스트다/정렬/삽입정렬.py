item = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
current = 1
while current < len(item):
    for i in range(current, 0, -1):
        if item[i] < item[i - 1]:
            item[i], item[i - 1] = item[i - 1], item[i]
        else:
            break
    current += 1

print(item)
