N = int(input())
move = list(input().split(' '))

current = [1, 1]
for m in move:
    if m == 'R' and current[1] == N:
        continue
    elif m == 'L' and current[1] == 1:
        continue
    elif m == 'U' and current[0] == 1:
        continue
    elif m == 'D' and current[0] == N:
        continue

    if m == 'R':
        current[1] += 1
    elif m == 'L':
        current[1] -= 1
    elif m == 'U':
        current[0] -= 1
    elif m == 'D':
        current[0] += 1

print(current[0], current[1])
