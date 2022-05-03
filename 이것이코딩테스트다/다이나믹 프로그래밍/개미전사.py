N = int(input())
storage = list(map(int, input().split()))

tt = 0
for n in range(N - 2, -1, -2):
    tt += storage[n]

yy = 0
for n in range(N - 1, 0, -2):
    yy += storage[n]


print(max(tt, yy))
