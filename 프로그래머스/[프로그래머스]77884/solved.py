def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        cnt = len(yaksu(n))
        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer


def yaksu(number):
    numbs = range(1, number + 1)
    result = []
    for i in numbs:
        if number % i == 0:
            result.append(i)
    return result
