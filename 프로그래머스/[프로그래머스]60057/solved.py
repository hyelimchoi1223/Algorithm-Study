def compress_text(context, byte):
    idx = 0
    count = 1
    result = ""
    before = context[0:byte]

    for j in range(byte, len(context), byte):
        if before == context[j : j + byte]:
            count += 1
        else:
            result += str(count) + before if count >= 2 else before
            count = 1
            before = context[j : j + byte]
    result += str(count) + before if count >= 2 else before
    return result


def solution(s):
    min_length = len(s)
    for i in range(1, len(s) // 2 + 1):
        length = len(compress_text(s, i))
        min_length = min(min_length, length)

    return min_length


print(solution("a"))
# solution("ababcdcdababcdcd")
# solution("abcabcdede")
# solution("abcabcabcabcdededededede")
# solution("xababcdcdababcdcd")
