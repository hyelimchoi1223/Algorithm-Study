N, K = map(int, input().split())
coins = []
for i in range(N):
  coins.append(int(input()))

count = 0
for i in reversed(coins):
  count += K//i
  K = K%i  

print(count)
