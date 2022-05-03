X = int(input())

result = X
min_count = 99999


def make_one(value, count=0):
    global min_count
    if value == 1:
        return count

    if value % 5 == 0:
        temp = make_one(value // 5, count + 1)
        if temp < min_count:
            min_count = temp

    if value % 3 == 0:
        temp = make_one(value // 3, count + 1)
        if temp < min_count:
            min_count = temp

    if value % 2 == 0:
        temp = make_one(value // 2, count + 1)
        if temp < min_count:
            min_count = temp

    temp = make_one(value - 1, count + 1)
    if temp < min_count:
        min_count = temp

    return min_count


print(make_one(X))
