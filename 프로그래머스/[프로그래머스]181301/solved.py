numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
           'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def solution(s):
    answer = 0
    word = ''
    answer_temp = ''
    for char in s:
        try:
            answer_temp += str(int(char))
        except:
            word += char
            if word in numbers:
                answer_temp += str(numbers[word])
                word = ''
    answer = int(answer_temp)
    return answer
