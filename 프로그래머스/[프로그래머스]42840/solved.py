import itertools


def match_answers_count(solvs, ans):
    solvs_ = make_student_solv(solvs, ans)
    result = list(map(lambda x, y: x is y, solvs_, ans)).count(True)
    return result


def make_student_solv(solvs, ans):
    answers_len = len(ans)
    it = itertools.cycle(solvs)
    result = [next(it) for _ in range(answers_len)]
    return result


def solution(answers):
    s_1 = [1, 2, 3, 4, 5]
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [match_answers_count(s_1, answers),
              match_answers_count(s_2, answers),
              match_answers_count(s_3, answers)]
    max_value = max(scores)
    answer = [i + 1 for i, value in enumerate(scores) if value == max_value]

    return answer
