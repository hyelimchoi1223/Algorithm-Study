def solution(d, budget):
    answer = 0
    d.sort()

    sum_temp = 0
    for i in d:
        sum_temp += i
        if sum_temp > budget:
            break
        answer += 1
    return answer
