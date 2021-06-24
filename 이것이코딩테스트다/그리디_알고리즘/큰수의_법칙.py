# 큰 수의 법칙
# 입력 조건 : 첫번째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분.
# 입력으로 주어지는 K는 M보다 항상 작거나 같다.
# 출력 조건 : 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

result = 0
count = 0
for i in range(M):
    if count < K:
        result += nums[0]
        count += 1
    else:
        result += nums[1]
        count = 0
print(result)
