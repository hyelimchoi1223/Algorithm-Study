count = 3
mul = 1
while True:
    if count == 0:
        break
    mul *= int(input())
    count -=1

result = []
result = [0 for _ in range(1, 11)]

for _ in str(mul):
    index = int(_)
    result[index] += 1
[print(i) for i in result]