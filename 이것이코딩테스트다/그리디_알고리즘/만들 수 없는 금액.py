# 풀이 방법
# 빈 배열을 만든다. 개수는 배열의 전체 합
# 조합의 합을 구해 만든 배열의 각 자리(인덱스)에 넣는다.
# 0은 존재하지 않는 조합이므로 0을 갖는 최소 인덱스를 구한다.
N = int(input())
coins = map(int, input().split())

coins = sorted(coins)
temp = [0] * (sum(coins) + 1)

for c in coins:
    temp[c] = 1

idx = 0
flag = 1
while True:
    if flag > len(coins):
        break
    if idx == len(coins):
        idx = 0
        flag += 1

    flag_value = coins[idx : idx + flag]
    before_sum = sum(flag_value)
    if len(flag_value) == flag:
        for sub in coins[idx + flag :]:
            temp[before_sum + sub] = 1

    idx += 1


min_index = 0
for idx, t in enumerate(temp[1:], 1):
    if t == 0:
        min_index = idx
        break
print(min_index)
