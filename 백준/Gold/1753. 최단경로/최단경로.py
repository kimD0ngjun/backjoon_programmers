import sys
import heapq
from collections import defaultdict


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# 다익스트라 함수
def dijkstra(graph, start):
    inf = float("inf")
    min_distances = {vertex: inf for vertex in graph}
    min_distances[start] = 0

    queue = []
    heapq.heappush(queue, (min_distances[start], start))

    while queue:
        cur_distance, cur_vertex = heapq.heappop(queue)

        if min_distances[cur_vertex] < cur_distance:
            continue

        # 간선 정보는 (인접 정점, 가중치) 튜플 형태로 저장
        for adj_vertex, weight in graph[cur_vertex]:  
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_vertex))

    return min_distances


# 입력 처리
vertexes, edges = map(int, sys_input().split())
start = int(sys_input())

graph = defaultdict(list)

for i in range(1, vertexes + 1):
    graph[i]  # 키에러 방지

for _ in range(edges):
    vertex, adj_vertex, weight = map(int, sys_input().split())
    graph[vertex].append((adj_vertex, weight))  # 간선 정보 리스트 할당

min_distance = dijkstra(graph, start)

for vertex in range(1, vertexes + 1):
    if vertex == start:
        print(0)
    elif min_distance[vertex] < float('inf'):
        print(min_distance[vertex])
    else:
        print("INF")
