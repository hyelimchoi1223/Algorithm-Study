S = list(map(int, list(input())))

answer = 0
current_group = [0, 0]
before = S[0]
for idx, s in enumerate(S[1:], 1):
    if before != s:
        current_group[before] += 1
        before = s
    if idx >= len(S) - 1:
        current_group[s] += 1

print(min(current_group))
