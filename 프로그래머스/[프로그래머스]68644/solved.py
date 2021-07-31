import itertools


def solution(numbers):

    answer = [x+y for x, y in itertools.permutations(numbers, 2)]
    answer = list(set(answer))
    answer.sort()
    return answer
