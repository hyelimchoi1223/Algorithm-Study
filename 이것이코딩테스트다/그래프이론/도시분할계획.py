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


N, M = map(int, input().split())
edge = []
parent = [0] * (N + 1)

for p in range(N + 1):
    parent[p] = p

for m in range(M):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))

edge = sorted(edge, key=lambda x: x[2])

result = 0
last = 0
for a, b, w in edge:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += w
        last = w

print(result - last)
