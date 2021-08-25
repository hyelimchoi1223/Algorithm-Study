def get_number(text):
    if '-' in text:
        text = text.replace('-', '')
        return int(text)*-1
    else:
        return int(text)


def solution(s):
    temp = list(map(int, s.split(' ')))
    answer = f"{str(min(temp))} {str(max(temp))}"
    return answer


solution