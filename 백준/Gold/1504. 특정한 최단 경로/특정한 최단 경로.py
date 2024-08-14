"""
https://www.acmicpc.net/problem/1339
"""
import heapq
import sys


# 입력
# 그래프 생성 함수
def dijkstra(start, graph, min_distances):
    queue = []
    heapq.heappush(queue, [0, start])
    min_distances[start] = 0

    while queue:
        cur_distance, cur_vertex = heapq.heappop(queue)

        # 최적화
        if cur_distance > min_distances[cur_vertex]:
            continue

        for weight, adj_vertex in graph[cur_vertex]:
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                heapq.heappush(queue, [updated_distance, adj_vertex])


# Read input
N, E = map(int, input().split())

# Initialize graph
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append([weight, end])
    graph[end].append([weight, start])

V1, V2 = map(int, input().split())

# 1 -> V1 -> V2 -> N // 1 -> V2 -> V1 -> N
# 두 가지 다 연산
inf = float('inf')
two_distances = [inf, inf]

# 1 -> V1, 1 -> V2
# 시작 지점은 공통이니까
path = [inf] * (N + 1)
dijkstra(1, graph, path)

# 연결이 한 곳이라도 안 된 케이스와 된 곳 비교
if path[V1] == inf or path[V2] == inf or path[N] == inf:
    print(-1)
else:
    two_distances[0] = path[V1]
    two_distances[1] = path[V2]

    # V1 -> V2, V2 -> V1
    path = [inf] * (N + 1)
    dijkstra(V1, graph, path)

    two_distances[0] += path[V2]
    two_distances[1] += path[V2]

    # V1 -> N
    two_distances[1] += path[N]

    # V2 -> N
    path = [inf] * (N + 1)
    dijkstra(V2, graph, path)

    two_distances[0] += path[N]

    print(min(two_distances))