N = int(input())
storage = list(map(int, input().split()))
dp = [0] * 100

dp[0] = 0
dp[1] = max(storage[0], storage[1])
for n in range(2, N):
    dp[n] = max(dp[n - 1], dp[n - 2] + storage[n])


print(dp[N - 1])
