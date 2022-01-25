from collections import deque


def solution(s):
    answer = 0
    s = deque(list(s))
    temp = []
    while True:
        if len(s) <= 0:
            break
        if len(temp) <= 0:
            temp.append(s.popleft())
            continue

        orgin = s.popleft()
        if temp[-1] != orgin:
            temp.append(orgin)
        elif temp[-1] == orgin:
            temp.pop()

    if len(temp) == 0:
        return 1
    else:
        return 0
