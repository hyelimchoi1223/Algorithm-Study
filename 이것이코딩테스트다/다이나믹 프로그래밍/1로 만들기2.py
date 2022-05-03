X = int(input())
dp = [0] * 999
result = X

for x in range(2, X + 1):
    dp[x] = dp[x - 1] + 1

    if x % 2 == 0:
        dp[x] = min(dp[x], dp[x // 2] + 1)
    if x % 3 == 0:
        dp[x] = min(dp[x], dp[x // 3] + 1)
    if x % 5 == 0:
        dp[x] = min(dp[x], dp[x // 5] + 1)

print(dp)
