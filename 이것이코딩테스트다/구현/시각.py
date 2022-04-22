N = int(input())

result = 0
for h in range(0, N + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            if (
                (h % 10 == 3 or h // 10 == 3)
                or (m % 10 == 3 or m // 10 == 3)
                or (s % 10 == 3 or s // 10 == 3)
            ):
                result += 1


print(result)
