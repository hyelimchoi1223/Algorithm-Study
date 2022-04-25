N = int(input())
temp = []
for n in range(N):
    temp.append(input())

temp = sorted(temp, reverse=True)
print(" ".join(temp))
