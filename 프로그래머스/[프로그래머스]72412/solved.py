# 효용성 테스트 통과 실패
def solution(info, query):
    answer = []
    info = [i.split(" ") for i in info]
    for q in query:
        q = q.replace(" and ", " ")
        q = q.split(" ")

        match = info
        for idx, qq in enumerate(q):
            if idx == len(q) - 1:
                match = [i for i in match if int(i[idx]) >= int(qq)]
            elif qq != "-":
                match = [i for i in match if i[idx] == qq]

        answer.append(len(match))
    return answer


result = solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
print(result)
