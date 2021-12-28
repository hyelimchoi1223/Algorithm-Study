def solution(lottos, win_nums):

    zero_count = lottos.count(0)
    match_count = 0
    for l in lottos:
        if l in win_nums:
            match_count += 1

    max_rank = get_rank(zero_count + match_count)
    min_rank = get_rank(match_count)
    answer = [max_rank, min_rank]
    return answer


def get_rank(match_num):
    if match_num == 6:
        return 1
    elif match_num == 5:
        return 2
    elif match_num == 4:
        return 3
    elif match_num == 3:
        return 4
    elif match_num == 2:
        return 5
    else:
        return 6
