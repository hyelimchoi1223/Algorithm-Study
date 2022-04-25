N = int(input())
temp = []
for n in range(N):
    temp.append(tuple(input().split()))

temp = sorted(temp, key=lambda x: x[1])
for t in temp:
    print(t[0], end=" ")
