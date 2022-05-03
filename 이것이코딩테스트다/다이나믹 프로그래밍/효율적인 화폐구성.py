N, M = map(int, input().split())
money = []

for n in range(N):
    money.append(int(input()))

dp = [100001] * (M + 1)
dp[0] = 0
for n in money:
    if n < M:
        dp[n] = 1

for m in range(4, M + 1):
    for n in money:
        if dp[m - n] != 10001:
            dp[m] = min(dp[m], dp[m - n] + 1)

if dp[-1] == 100001:
    print(-1)
else:
    print(dp[-1])


print(dp)
