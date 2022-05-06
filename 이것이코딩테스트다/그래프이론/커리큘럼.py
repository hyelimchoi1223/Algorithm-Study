from collections import deque
import copy


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


N = int(input())
time = [0] * (N + 1)
classes = [[] for n in range(N + 1)]
indegree = [0] * (N + 1)
for n in range(1, N + 1):
    temp = list(map(int, input().split()))
    time[n] = temp[0]
    for t in temp[1:]:
        if t == -1:
            break
        classes[t].append(n)
        indegree[n] += 1

queue = deque([])
for n in range(1, N + 1):
    if indegree[n] == 0:
        queue.append(n)

result = copy.deepcopy(time)
while queue:
    now = queue.popleft()

    for c in classes[now]:
        result[c] = max(result[c], result[now] + time[c])
        indegree[c] -= 1
        if indegree[c] == 0:
            queue.append(c)

for t in result[1:]:
    print(t)
