def solution(numbers, hand):
    answer = ""
    number_pos = {}
    num = 1
    for i in range(1, 4, 1):
        for j in range(1, 4, 1):
            number_pos[num] = (i, j)
            num += 1

    number_pos["*"] = (4, 1)
    number_pos[0] = (4, 2)
    number_pos["#"] = (4, 3)

    left_pos = "*"
    right_pos = "#"

    for n in numbers:
        if n in [1, 4, 7]:
            left_pos = n
            answer += "L"
        elif n in [3, 6, 9]:
            right_pos = n
            answer += "R"
        else:
            left = abs(number_pos[left_pos][0] - number_pos[n][0]) + abs(
                number_pos[left_pos][1] - number_pos[n][1]
            )
            right = abs(number_pos[right_pos][0] - number_pos[n][0]) + abs(
                number_pos[right_pos][1] - number_pos[n][1]
            )

            if left > right:
                right_pos = n
                answer += "R"
            elif left < right:
                left_pos = n
                answer += "L"
            else:
                if hand == "left":
                    left_pos = n
                    answer += "L"
                else:
                    right_pos = n
                    answer += "R"

    return answer
