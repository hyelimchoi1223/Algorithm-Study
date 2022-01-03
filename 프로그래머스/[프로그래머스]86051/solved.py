def solution(numbers):
    answer = 0
    max_num = 9
    for n in range(max_num + 1):
        if n not in numbers:
            answer += n
    return answer


solution([1, 2, 3, 4, 6, 7, 8, 0])
