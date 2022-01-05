def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if s:
            answer += a * 1
        else:
            answer += a * -1
    return answer
