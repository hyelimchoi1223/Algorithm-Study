from collections import Counter


def solution(id_list, report, k):
    answer = []
    user_declare = {}
    total = []
    for r in report:
        user, declare = r.split(" ")
        if user in user_declare.keys() and declare in user_declare[user]:
            continue

        if user not in user_declare:
            user_declare[user] = []

        user_declare[user].append(declare)
        total.append(declare)

    future_block = [idx for idx, cnt in Counter(total).items() if cnt >= k]

    for i in id_list:
        if i not in user_declare:
            answer.append(0)
        else:
            count = 0
            for u in user_declare[i]:
                if u in future_block:
                    count += 1

            answer.append(count)
    return answer
