def hansu(a):
    result_array = list(map(int, str(a)))
    gap_array = []
    if result_array.__len__() == 1:
        gap_array = [i for i in result_array]
    else:
        gap_array = [result_array[_-1]-result_array[_]
                     for _ in range(1, result_array.__len__())]
    return list(set(gap_array)).__len__()


n = int(input())
result = 0
for _ in range(1, n+1):
    count = hansu(_)
    if count == 1:
        result += 1

print(result)
