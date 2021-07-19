pay = 1000-int(input())
money = [500, 100, 50, 10, 5, 1]

count = 0
for i in money:
    count += pay//i
    pay %= i

print(count)
