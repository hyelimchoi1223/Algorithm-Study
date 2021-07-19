def solution(a, b):
    answer = 0
    if a == b:
        return a
    step = 1
    if a > b:
        step = -1
    answer = sum(list(range(a, b+step, step)))
    return answer
