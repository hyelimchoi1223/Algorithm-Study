N = int(input())
dp = [0] * (N + 1)
count = 0
dp[1] = 1
dp[2] = 3
for i in range(3, N + 1):
    dp[3] = (dp[i - 1] + (dp[i - 2] * 2)) % 796796

print(dp[-1])
