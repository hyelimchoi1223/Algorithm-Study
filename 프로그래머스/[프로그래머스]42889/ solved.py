def solution(N, stages):

    stage_fail_dict = {}
    for n in range(1, N + 1):
        people_cnt = len([s for s in stages if s >= n])
        if people_cnt == 0:
            fail_rate = 0
        else:
            fail_rate = stages.count(n) / people_cnt
        stage_fail_dict[n] = fail_rate

    return sorted(stage_fail_dict, key=lambda x: stage_fail_dict[x], reverse=True)
