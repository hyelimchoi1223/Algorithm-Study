N = int(input())
time = list(map(int, input().split()))
time = sorted(time)

result = 0
for i in range(N):
    temp = 0
    if i == 0:
        result += time[i]
        continue
    result += sum(time[:i+1])

print(result)
