# 풀이 방법
# target : 만들 수 있는지 체크
# 화폐가 작은 단위부터 하나씩 확인해 target을 업데이트
N = int(input())
coins = map(int, input().split())

coins = sorted(coins)

target = 1
for c in coins:
    if c > target:
        break

    target += c

print(target)
