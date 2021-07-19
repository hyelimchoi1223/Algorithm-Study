from itertools import cycle


def solution(n):
    src = "수박"
    temp = [item for _, item in zip(range(n), cycle(src))]
    answer = ''.join(temp)
    return answer
