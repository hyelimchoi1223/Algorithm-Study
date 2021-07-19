N = int(input())
moves = list(input().split())
current = [1, 1]
for i in moves:
    index = 0
    temp = 0
    if i == "R":
        temp = current[1]+1
        index = 1
    elif i == "L":
        temp = current[1]-1
        index = 1
    elif i == "U":
        temp = current[0]-1
        index = 0
    elif i == "D":
        temp = current[0]+1
        index = 0

    if temp > 0:
        current[index] = temp

print(*current)
