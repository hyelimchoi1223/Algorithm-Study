N = int(input())
prices = []
for i in range(N):
    prices.append(int(input()))

prices.sort(reverse=True)
result = 0
for i in range(N//3):
    result += sum(prices[i*3:3*(i+1)])-min(prices[i*3:3*(i+1)])

if N % 3:
    result += sum(prices[(N // 3)*3:])

print(result)
