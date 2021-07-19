# solution 1
from collections import Counter


def solution(participant, completion):

    temp = Counter(participant)-Counter(completion)
    answer, value = temp.popitem()

    return answer
