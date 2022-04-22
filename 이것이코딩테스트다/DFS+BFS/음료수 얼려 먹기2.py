N, M = map(int, input().split())
map_table = []
for n in range(N):
    map_table.append(list(input()))


def discover(row, col):
    if row < 0 or row >= N or col < 0 or col >= M:
        return False

    if map_table[row][col] == "0":
        map_table[row][col] = "1"
        discover(row, col - 1)
        discover(row - 1, col)
        discover(row + 1, col)
        discover(row, col + 1)
        return True
    return False


result = 0
for n in range(N):
    for m in range(M):
        if discover(n, m):
            result += 1


print(result)
