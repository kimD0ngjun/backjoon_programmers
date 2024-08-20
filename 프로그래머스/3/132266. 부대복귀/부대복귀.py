"""
https://school.programmers.co.kr/learn/courses/30/lessons/132266
"""
import heapq


def solution(n, roads, sources, destination):
    # 그래프 초기화
    graph = {node: {} for node in range(1, n + 1)}

    for road in roads:
        graph[road[0]][road[1]] = 1
        graph[road[1]][road[0]] = 1

    # 각 소스로부터 목적지까지의 최단거리가 아닌, 반대로 목적지에서 각 지점까지의 최소 거리
    # 목적지에서 다른 모든 노드까지의 최단 거리를 계산
    INF = float("inf")
    min_distances = [INF] * (n + 1)
    min_distances[destination] = 0

    queue = []
    heapq.heappush(queue, (0, destination))

    while queue:
        cur_distance, cur_vertex = heapq.heappop(queue)

        if min_distances[cur_vertex] < cur_distance:
            continue

        for adj_vertex, weight in graph[cur_vertex].items():
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_vertex))

    answer = []

    for source in sources:
        if min_distances[source] == INF:
            answer.append(-1)
        else:
            answer.append(min_distances[source])

    return answer