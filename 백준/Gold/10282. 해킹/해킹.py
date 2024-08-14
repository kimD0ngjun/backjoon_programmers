"""
https://www.acmicpc.net/problem/10282
"""
import heapq


# HashMap 기반 그래프 다익스트라
def dijkstra(graph, start, n):
    inf = float("inf")
    min_distances = [inf] * (n + 1)
    min_distances[start] = 0

    queue = []
    heapq.heappush(queue, (min_distances[start], start))

    while queue:
        cur_distance, cur_dir_vertex = heapq.heappop(queue)

        if min_distances[cur_dir_vertex] < cur_distance:
            continue

        for adj_vertex, weight in graph[cur_dir_vertex].items():
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_vertex))

    computer_count = 0
    infected_time = 0

    for i in range(1, n + 1):
        if min_distances[i] != inf:
            computer_count += 1
            infected_time = max(infected_time, min_distances[i])

    return computer_count, infected_time


# 입력
T = int(input())

for i in range(T):

    n, d, c = map(int, input().split())
    graph = {i: {} for i in range(1, n + 1)}  # 각 케이스별 그래프 초기화

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b][a] = s

    # print("케이스 {}: {}".format(i + 1, graph))

    count, time = dijkstra(graph, c, n)
    print(count, time)
