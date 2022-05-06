from collections import deque

V, E = map(int, input().split())
graph = [[] for i in range(V + 1)]
indegree = [0] * (V + 1)
indegree[0] = int(1e9)
for e in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque([])
for i in range(1, V + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for j in graph[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)

for r in result:
    print(r, end=" ")
