data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

temp = [0] * (max(data) + 1)

for d in data:
    temp[d] += 1

for idx, t in enumerate(temp):
    for i in range(t):
        print(str(idx), end=" ")
