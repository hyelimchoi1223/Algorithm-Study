def solution(n):
    answer = 0
    result_calc = []
    while True:
        if n == 0:
            break
        result_calc.append(n % 3)
        n = n // 3

    zisu = 0
    while True:
        if len(result_calc) == 0:
            break
        answer += result_calc.pop() * (3 ** zisu)
        zisu += 1

    return answer


print(solution(45))
