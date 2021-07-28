def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer
