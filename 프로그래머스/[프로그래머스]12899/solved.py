def solution(n):
    answer = ''
    remain = []
    while n > 0:
        if n % 3 == 0:
            remain.append(4)
            n = n//3-1
        else:
            remain.append(n % 3)
            n = n//3

    answer = ''.join(map(str, remain[::-1]))
    return answer


print(solution(6))
solution(7)
solution(10)
solution(9)
