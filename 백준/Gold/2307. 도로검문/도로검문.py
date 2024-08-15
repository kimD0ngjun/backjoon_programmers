"""
https://www.acmicpc.net/problem/2307
"""
import heapq
from collections import defaultdict

INF = float("inf")


def dijkstraWithPrintPath(graph, start, n):
    min_distances = [INF] * (n + 1)
    min_paths = [[] for _ in range(n + 1)]  # 경로 저장용 리스트
    min_distances[start] = 0

    queue = []
    heapq.heappush(queue, (min_distances[start], start, [start]))

    while queue:
        cur_distance, cur_vertex, cur_path = heapq.heappop(queue)

        if min_distances[cur_vertex] < cur_distance:
            continue

        for adj_vertex, weight in graph[cur_vertex].items():
            updated_distance = cur_distance + weight
            temp_path = cur_path + [adj_vertex]

            if updated_distance < min_distances[adj_vertex]:
                min_distances[adj_vertex] = updated_distance
                min_paths[adj_vertex] = temp_path
                heapq.heappush(queue, (updated_distance, adj_vertex, temp_path))

    return min_distances[n], min_paths[n]


# 입력
N, M = map(int, input().split())

# 그래프 초기화: defaultdict 사용
graph = defaultdict(dict)

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t

# 최소 경로 산출
min_distance, min_path = dijkstraWithPrintPath(graph, 1, N)

# 지연 시간 연산
delay = 0

for i in range(len(min_path) - 1):
    a, b = min_path[i], min_path[i + 1]

    # 그래프 복사
    temp = defaultdict(dict, {k: v.copy() for k, v in graph.items()})

    # 해당 경로 삭제
    if b in temp[a]:
        del temp[a][b]
    if a in temp[b]:
        del temp[b][a]

    new_min_distance, _ = dijkstraWithPrintPath(temp, 1, N)

    if new_min_distance == INF:
        delay = -1
        break
    delay = max(delay, new_min_distance - min_distance)

# 출력
print(delay)
