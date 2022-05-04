graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    [],
]
# 내 풀이
# visit = [False] * 7
# infinite = int(1e9)
# distances = [infinite] * 7
# start = 1
# distances[start] = 0
# visit[start] = True

# while True:
#     visit[start] = True
#     if start == 6:
#         break

#     for n, g in graph[start]:
#         if visit[n] == False:
#             distances[n] = min(distances[n], distances[start] + g)

#     # min distances
#     min_value = infinite
#     min_index = 0
#     for idx, d in enumerate(distances):
#         if min_value > d and visit[idx] == False:
#             min_value = d
#             min_index = idx

#     start = min_index

# print(distances[6])

# 예제 풀이 - 일반
visit = [False] * 7
INF = int(1e9)
distances = [INF] * 7


# def get_smallest_node():
#     min_value = INF
#     min_index = 0
#     for idx, d in enumerate(distances):
#         if min_value > d and not visit[idx]:
#             min_value = d
#             min_index = idx

#     return min_index


# def dijkstra(start):
#     distances[start] = 0
#     visit[start] = True
#     for node, edge in graph[start]:
#         distances[node] = edge

#     for i in range(len(distances) - 1):
#         now = get_smallest_node()
#         visit[now] = True

#         for n, g in graph[now]:
#             if visit[n] == False:
#                 distances[n] = min(distances[n], distances[now] + g)


# dijkstra(1)

# for i in distances[1:]:
#     if i == INF:
#         print("Infinity")
#     else:
#         print(i)


# 예제풀이 - 개선된 방법
import heapq


def dijkstra2(start):
    priority = []
    distances[start] = 0
    visit[start] = True

    heapq.heappush(priority, (distances[start], start))
    while priority:
        dist, now = heapq.heappop(priority)
        if distances[now] < dist:
            continue

        visit[now] = True
        for n, g in graph[now]:
            if visit[n] == False:
                distances[n] = min(distances[n], dist + g)
                heapq.heappush(priority, (distances[n], n))


dijkstra2(1)

for i in distances[1:]:
    if i == INF:
        print("Infinity")
    else:
        print(i)
