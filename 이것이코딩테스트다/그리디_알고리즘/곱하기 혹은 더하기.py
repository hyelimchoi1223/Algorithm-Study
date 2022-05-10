S = list(map(int, list(input())))

answer = 0
for s in S:
    if s <= 1 or answer <= 1:
        answer += s
    else:
        answer *= s

print(answer)
