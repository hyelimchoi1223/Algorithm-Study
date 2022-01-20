def solution(price, money, count):
    answer = 0

    total = 0
    for i in range(1, count + 1):
        total += price * i

    if money <= total:
        answer = total - money

    return answer


print(solution(3, 20, 4))
