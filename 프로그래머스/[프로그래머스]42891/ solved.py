import heapq


def solution(food_times, K):
    if sum(food_times) <= K:
        return -1

    answer = 0
    queue = []
    for idx, time in enumerate(food_times):
        heapq.heappush(queue, (time, idx + 1))

    sum_value = 0
    last_time = 0
    length = len(food_times)
    while sum_value + ((queue[0][0] - last_time) * length) <= K:
        time, food = heapq.heappop(queue)
        sum_value += (time - last_time) * length
        length -= 1
        last_time = time

    queue = sorted(queue, key=lambda x: x[1])
    return queue[(K - sum_value) % length][1]


print(solution([3, 1, 2], 5))
