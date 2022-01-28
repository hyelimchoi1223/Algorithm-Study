def solution(n):
    answer = []
    answer = list(str(n))
    answer = list(map(int, answer))
    answer = answer[::-1]
    return answer
