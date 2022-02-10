T = int(input())

max_score = 0
for t in range(T):
    answer = 0
    i = 0
    N = list(map(int, input().split(" ")))
    for num in N:
        cnt = N.count(num)
        if cnt == 3:
            answer = 10000 + num * 1000
        elif cnt == 2:
            answer = 1000 + num * 100
        else:
            if len(N) == i + 1:
                answer = max(N) * 100
            else:
                i += 1

    if max_score < answer:
        max_score = answer


print(max_score)
