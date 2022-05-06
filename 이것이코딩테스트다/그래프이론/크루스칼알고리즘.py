def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


V, E = map(int, input().split())
graph = []
parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

for e in range(E):
    start, end, weight = map(int, input().split())
    graph.append((start, end, weight))


cost = 0
graph = sorted(graph, key=lambda x: x[2])
for a, b, w in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += w

print(cost)
