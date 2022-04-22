from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9
v = 1
temp = deque([])
temp.append(v)
visited[v] = True
while temp:
    current = temp.popleft()

    print(current, end=" ")

    for i in graph[current]:
        if not visited[i]:
            temp.append(i)
            visited[i] = True
