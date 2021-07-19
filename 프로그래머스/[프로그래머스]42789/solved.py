def solution(array, commands):
    answer = []
    for start, end, index in commands:
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[index-1])
    return answer
