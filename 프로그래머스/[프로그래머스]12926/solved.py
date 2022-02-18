def solution(s, n):
    answer = ""
    for t in s:
        temp_num = ord(t) + n
        if t.isupper():
            if temp_num > 90:
                temp_num = temp_num - 26
        elif t.islower():
            if temp_num > 122:
                temp_num = temp_num - 26
        else:
            answer += t
            continue
        answer += chr(temp_num)

    return answer
