"""
https://www.acmicpc.net/problem/16118
"""
import heapq
from collections import defaultdict

INF = float("inf")


# 토끼의 다익스트라
def rabbit():
    min_distances = [INF] * (N + 1)
    min_distances[1] = 0

    queue = []
    heapq.heappush(queue, (min_distances[1], 1))

    while queue:
        cur_distance, cur_dir_vertex = heapq.heappop(queue)

        if min_distances[cur_dir_vertex] < cur_distance:
            continue

        for adj_vertex, weight in graph[cur_dir_vertex].items():
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_vertex))

    return min_distances


# 늑대의 다익스트라
def wolf():
    # 해당 노드까지의 최소 거리
    # 늑대는 지친 상태로 도착하거나 보충된 상태로 도착할 두 가지 가능성 존재, 각각 따로 관리
    # 인덱스 0: 보충, 인덱스 1: 지침
    min_distances = [[INF] * 2 for _ in range(N + 1)]
    min_distances[1][0] = 0

    queue = []
    heapq.heappush(queue, (0, 1, True))  # 거리, 노드, 체력

    while queue:
        cur_distance, cur_vertex, cur_energy = heapq.heappop(queue)

        # 에너지 상태에 따라서 도달한 노드까지의 최소 거리 각자 추적
        if cur_energy:
            energy_idx = 0
        else:
            energy_idx = 1

        # 그 상태에 따라 도달한 노드까지의 최소 거리 로직 최적화
        if min_distances[cur_vertex][energy_idx] < cur_distance:
            continue

        for adj_vertex, weight in graph[cur_vertex].items():

            # 에너지에 따른 가중치 추가 계산
            if cur_energy:
                updated_distance = cur_distance + weight / 2
            else:
                updated_distance = cur_distance + weight * 2

            next_energy = not cur_energy

            # 다음 상태
            if next_energy:
                next_energy_idx = 0
            else:
                next_energy_idx = 1

            if updated_distance < min_distances[adj_vertex][next_energy_idx]:
                min_distances[adj_vertex][next_energy_idx] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_vertex, next_energy))

    return list(map(lambda n: min(n[0], n[1]), min_distances))


# 입력
N, M = map(int, input().split())  # 그루터기(노드) 개수(N), 오솔킬(간선) 개수(M)

# 그래프 초기화
graph = {node: {} for node in range(1, N + 1)}

for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a][b] = d  # 거리(가중치)
    graph[b][a] = d  # 양방향


# 연산
rabbit_path = rabbit()
wolf_path = wolf()

# print("토끼: {}", rabbit_path)
# print("늑대: {}", wolf_path)

result = 0

for i in range(1, N + 1):
    if rabbit_path[i] < wolf_path[i]:
        result += 1

print(result)
