def solution(s):
    s = s.replace("{{", "")
    s = s.replace("}}", "")
    s = s.split("},{")
    s = [txt.split(",") for txt in s]
    s.sort(key=lambda x: len(x))
    answer = []
    temp = ""
    for txt in s:
        if len(answer) == 0:
            answer.append(int(txt[0]))
            continue

        remain = [t for t in txt if int(t) not in answer]
        if len(remain) != 0:
            answer.append(int(remain[0]))

    return answer
