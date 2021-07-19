N, L = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
for i in heights:
    if L >= i:
        L += 1
    else:
        break

print(L)
