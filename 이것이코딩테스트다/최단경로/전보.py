import heapq

N, M, C = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N + 1)
graph = [[] for n in range(N + 1)]
visited = [False] * (N + 1)
for m in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


def dijkstra(start):
    queue = []
    visited[start] = True
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    while queue:
        dist, now = heapq.heappop(queue)

        for g, d in graph[now]:
            if distance[g] < dist:
                continue
            if visited[g] == False:
                distance[g] = d
                heapq.heappush(queue, (min(d, dist + d), g))


dijkstra(C)
count = 0
max_time = 0
for d in distance:
    if d != INF and d != 0:
        count += 1
        max_time = max(max_time, d)
print(count, max_time)
