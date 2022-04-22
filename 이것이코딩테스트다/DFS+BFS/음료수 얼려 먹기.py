N, M = map(int, input().split(" "))
tray = []
for n in range(N):
    tray.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if tray[x][y] == 0:
        tray[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


answer = 0
for n in range(N):
    for m in range(M):
        if dfs(n, m) == True:
            answer += 1


print(answer)
