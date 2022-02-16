def solution(nums):
    N = len(nums)
    set_N = len(set(nums))
    if set_N > N // 2:
        return N // 2
    else:
        return set_N
