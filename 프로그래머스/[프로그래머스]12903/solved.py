def solution(s):
    answer = ''
    str_length = len(s)
    if str_length % 2 == 0:
        index = str_length//2
        answer = s[index-1]+s[index]
    else:
        index = str_length//2
        answer = s[index]

    return answer
