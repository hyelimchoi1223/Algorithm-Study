def solution(n):
    answer = 0
    temp = list(str(n))
    temp = list(map(int, temp))
    answer = sum(temp)
    return answer
