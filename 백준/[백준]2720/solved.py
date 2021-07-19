def GetBalance(pay):
    coins = [25, 10, 5, 1]
    temp = pay
    result = []
    for i in coins:
        result.append(temp//i)
        temp %= i
    return result


T = int(input())
result = []
for i in range(T):
    pay = int(input())
    print(*GetBalance(pay), end=' ')
