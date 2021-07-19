N = int(input())
lopes = []
for i in range(N):
    lopes.append(int(input()))

max_weight = 0
for i in range(N):
    mini_lopes = lopes[i:]
    min_lopes = min(mini_lopes)
    count = len(mini_lopes)
    if max_weight < min_lopes*count:
        max_weight = min_lopes*count

print(max_weight)
