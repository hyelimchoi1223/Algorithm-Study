INF = int(1e9)
distance = [[INF] * 5 for i in range(5)]

graph = [[], [(2, 4), (4, 6)], [(1, 3), (3, 7)], [(1, 5), (4, 4)], [(3, 2)]]

for i, v in enumerate(distance):
    for j, m in enumerate(v):
        if i == j:
            distance[i][j] = 0

for now, g in enumerate(graph):
    for n, e in g:
        distance[now][n] = e

for k in range(1, len(distance)):
    for a in range(1, len(distance)):
        for b in range(1, len(distance)):
            if a == b:
                continue

            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for g in distance[1:]:

    for d in g[1:]:
        print(d, end=" ")

    print("\n")
