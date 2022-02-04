def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a = []
        for r1, r2 in zip(a1, a2):
            a.append(r1 + r2)
        answer.append(a)
    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
