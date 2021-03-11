count = int(input())

for _ in range(count):
    k = int(input())
    n = int(input())
    base = [[_ for _ in range(1, n+1)]]
    value = []
    for item in range(1, k+1):
        value.append(sum(base[item-1][:n]))
    base.append(value)

print(base)
    