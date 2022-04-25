import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
ddeok = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(ddeok)

result = 0
while True:
    center = (start + end) // 2

    if start > end:
        break

    value = sum([d - center for d in ddeok if d > center])
    if value > M:
        start = center + 1
    else:
        result = center
        end = center - 1


print(result)
