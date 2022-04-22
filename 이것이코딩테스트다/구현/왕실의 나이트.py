pos = input()
col, row = pos[0], int(pos[1])
count = 0
night = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
for i in night:
    x, y = ord(col) + i[0], row + i[1]

    if (ord("a") <= x and x <= ord("h")) and (1 <= y and y <= 8):
        count += 1

print(count)
