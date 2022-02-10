N = list(map(int, input().split(" ")))

answer = 0
i = 0
while True:
    num = N[i]
    cnt = N.count(num)
    if cnt == 3:
        answer = 10000 + num * 1000
        break
    elif cnt == 2:
        answer = 1000 + num * 100
        break
    else:
        if len(N) == i + 1:
            answer = max(N) * 100
            break
        else:
            i += 1


print(answer)
