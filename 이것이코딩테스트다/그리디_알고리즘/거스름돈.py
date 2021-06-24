# 카운터에 500원, 100원, 50원, 10원짜리 동전히 무한히 존재한다고
# 가정햇을 때 거슬러줘야할 동전의 최소 개수를 구해라.

balance = int(input())
coins = [500, 100, 50, 10]
count = 0
for i in coins:
    count += balance // i
    balance %= i

print(count)
