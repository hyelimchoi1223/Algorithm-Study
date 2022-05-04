N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for i in range(N + 1)]
for m in range(M):
    node, target = map(int, input().split())
    graph[node][target] = 1
    graph[target][node] = 1

X, K = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)
