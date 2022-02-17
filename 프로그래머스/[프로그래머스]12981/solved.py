def solution(n, words):
    answer = [0, 0]

    before = words[0]
    for idx, word in enumerate(words[1:], 1):
        if before[-1] != word[0] or word in words[:idx]:
            order, person = divmod(idx, n)
            return [person + 1, order + 1]
        else:
            before = word

    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
