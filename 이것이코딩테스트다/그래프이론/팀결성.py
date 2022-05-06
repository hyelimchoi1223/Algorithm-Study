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
parent = [0] * (N + 1)

for p in range(N + 1):
    parent[p] = p

for m in range(M):
    o, a, b = map(int, input().split())

    if o == 0:
        union_parent(parent, a, b)
    elif o == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
