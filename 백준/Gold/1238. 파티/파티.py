"""
https://www.acmicpc.net/problem/1238
"""
import heapq
from collections import defaultdict

INF = float("inf")


# 다익스트라(start에서 end까지의 최단거리 도출)
def dijkstra(graph, start, end):
    min_distances = {node: INF for node in graph}
    min_distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_distance, cur_vertex = heapq.heappop(queue)

        # 현재 정점이 도착점이라면 바로 리턴
        if cur_vertex == end:
            return cur_distance

        if cur_distance > min_distances[cur_vertex]:
            continue

        for adj_vertex, weight in graph[cur_vertex].items():
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_vertex))


# 입력
N, M, X = map(int, input().split())

# 그래프 초기화
graph = defaultdict(dict)

for _ in range(M):
    start, end, T = map(int, input().split())
    graph[start][end] = T


# 연산
time = 0

for i in range(1, N + 1):

    if i == X:
        continue

    go = dijkstra(graph, i, X)
    back = dijkstra(graph, X, i)

    # print("{}가 가는데 걸리는 시간: {} // 오는데 걸리는 시간: {}".format(i, go, back))
    # print(go + back)

    time = max(time, go + back)

print(time)