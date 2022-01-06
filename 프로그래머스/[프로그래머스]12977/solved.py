from itertools import combinations


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        i = list(i)
        if isprime(sum(i)):
            answer += 1

    return answer


def isprime(number):
    i = 2
    while i * i <= number:
        if number < 2:
            return True
        if number % i == 0:
            return False
        i += 1
    return True
