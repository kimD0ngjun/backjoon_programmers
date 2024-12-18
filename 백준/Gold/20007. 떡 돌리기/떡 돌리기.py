import heapq
from collections import defaultdict

INF = float("inf")

# input
N, M, X, Y = map(int, input().split())
graph = defaultdict(dict)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = C
    graph[B][A] = C


# 다익스트라 알고리즘
def dijkstra(start):
    min_distances = [INF] * N
    min_distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))  # 시작점의 거리: 0

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if cur_distance > min_distances[cur_node]:
            continue

        for adj_node, weight in graph[cur_node].items():
            updated_distance = cur_distance + weight

            if updated_distance < min_distances[adj_node]:
                min_distances[adj_node] = updated_distance
                heapq.heappush(queue, (updated_distance, adj_node))

    return min_distances


# 최소 일수 계산
def calculate():
    # 다익스트라로 Y번 집에서 모든 집까지의 최단 거리 계산
    distances = dijkstra(Y)

    # 예외 처리: 왕복이 불가능한 집이 있는 경우
    for distance in distances:
        if distance != INF and distance * 2 > X:  # 왕복이 불가능한 경우
            return -1

    # 가장 가까운 거리의 노드들부터 순차적으로 간선 가중치 합산
    sorted_distances = sorted((distances[i], i) for i in range(N) if i != Y)

    days = 0
    visited = [False] * N
    visited[Y] = True  # 시작점 방문 처리

    # 전부 방문할 때까지 연산
    while not all(visited):
        current_distance = 0  # 하루 동안 이동한 거리

        for i in range(len(sorted_distances)):
            distance, node = sorted_distances[i]
            if visited[node]:  # 이미 방문한 노드는 건너뜀
                continue

            # 왕복 거리(X)를 초과하지 않으면 방문
            if current_distance + (2 * distance) <= X:
                current_distance += 2 * distance
                visited[node] = True
            else:
                break

        days += 1  # 하루 경과

    return days


print(calculate())
