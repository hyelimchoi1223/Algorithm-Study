def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        print("Cycle 발생")
        break
    else:
        union_parent(parent, a, b)
