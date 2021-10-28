# n : 전체 학생 수, lost : 도난당한 학생 번호, reserve : 여벌의 체육복 가진 번호
def solution(n, lost, reserve):
    student = list(range(1, n+1))
    duplicate = [x for x in lost if x in reserve]
    # 여분을 가진 학생이 도난 당할 경우 처리
    for _ in duplicate:
        lost.remove(_)
        reserve.remove(_)
    _lost = lost.copy()

    for i in lost:
        current_index = student.index(i)
        if current_index-1 >= 0 and student[current_index-1] in reserve:
            reserve.remove(student[current_index-1])
            _lost.remove(i)
        elif len(student) != current_index+1 and student[current_index+1] in reserve:
            reserve.remove(student[current_index+1])
            _lost.remove(i)

    lost[:] = _lost
    result = [x for x in student if x not in _lost]
    answer = len(result)
    return answer
