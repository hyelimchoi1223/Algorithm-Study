from collections import deque

N, M = map(int, input().split())
map_table = []
for n in range(N):
    map_table.append(list(map(int, list(input()))))

temp = deque([])
start, end = (0, 0), (N - 1, M - 1)
temp.append(start)


while temp:
    current_n, current_m = temp.popleft()

    if current_m + 1 < M and map_table[current_n][current_m + 1] == 1:
        map_table[current_n][current_m + 1] += map_table[current_n][current_m]
        temp.append((current_n, current_m + 1))
    elif current_n + 1 < N and map_table[current_n + 1][current_m] == 1:
        map_table[current_n + 1][current_m] += map_table[current_n][current_m]
        temp.append((current_n + 1, current_m))

print(map_table)
print(map_table[end[0]][end[1]])
