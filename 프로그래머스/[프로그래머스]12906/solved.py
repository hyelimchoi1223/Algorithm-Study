from itertools import groupby


def solution(arr):
    answer = []
    group = groupby(arr)
    for key, items in group:
        answer.append(key)
    return answer
