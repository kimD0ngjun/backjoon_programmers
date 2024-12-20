import heapq
from collections import defaultdict

INF = float("inf")

# input
N, M = map(int, input().split())
stations = defaultdict(str)

for i in range(N):
    station = int(input())

    if station == 0:
        stations[i] = "A"
    else:
        stations[i] = "B"

graph = defaultdict(dict)

for i in range(N):
    weight_info = list(map(int, input().split()))

    for j in range(len(weight_info)):
        if i == j:
            continue

        if weight_info[j] != 0:
            graph[i][j] = weight_info[j]

# print(stations)
# print(graph)

"""
노드를 최소한 거치면서 최단 거리를 가야 함
우선사항 : 환승 최소 횟수, 그 중에서 소요시간 가장 짧은 케이스
"""


def dijkstra(start, end):
    min_distances = [[INF, INF] for _ in range(N)]  # 인덱스: 노드, (환승 횟수, 거리)
    min_distances[start] = [0, 0]

    queue = []
    heapq.heappush(queue, (0, 0, start))  # (거리, 환승 횟수, 노드)

    while queue:
        cur_distance, cur_count, cur_node = heapq.heappop(queue)

        if cur_distance > min_distances[cur_node][1]:
            continue

        for adj_node, weight in graph[cur_node].items():
            updated_distance = cur_distance + weight
            updated_count = cur_count

            if stations[adj_node] != stations[cur_node]:  # 환승 발생
                updated_count += 1

            # 새로운 환승 횟수가 기존 기록된 환승 횟수보다 적거나, 같으면서 거리도 짧은 경우 업데이트
            if (
                    updated_count < min_distances[adj_node][0] or
                    (updated_count == min_distances[adj_node][0] and updated_distance < min_distances[adj_node][1])
            ):
                min_distances[adj_node] = [updated_count, updated_distance]
                heapq.heappush(queue, (updated_distance, updated_count, adj_node))

    # print(min_distances)
    return min_distances[end]


min_distance = dijkstra(0, M)

print(str(min_distance[0]) + " " + str(min_distance[1]))
