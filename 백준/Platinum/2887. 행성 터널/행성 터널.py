import copy
import sys
import heapq


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# 간선 함수
# 삼차원 좌표 튜플 인자
def make_edge(vertex, adj_vertex, node_info):
    x1, y1, z1 = node_info[vertex]
    x2, y2, z2 = node_info[adj_vertex]

    return (adj_vertex, min(abs(x1-x2), abs(y1-y2), abs(z1-z2)))


# 프림 알고리즘
def prim(graph, start_vertex):
    connected = set()
    heap = []

    heapq.heappush(heap, (0, start_vertex))

    min_sum_weight = 0

    while heap:
        cur_weight, cur_vertex = heapq.heappop(heap)

        if cur_vertex not in connected:
            connected.add(cur_vertex)
            min_sum_weight += cur_weight

            for adj_weight, adj_vertex in graph[cur_vertex]:
                if adj_vertex not in connected:
                    heapq.heappush(heap, (adj_weight, adj_vertex))

    return min_sum_weight


# 입력 처리

vertexes = []
count = int(input())

for idx in range(count):
    x2, y2, z2 = map(int, sys_input().split())
    # x좌표, y좌표, z좌표, 노드(정점) 지칭 정보
    vertexes.append((x2, y2, z2, idx))

vertexes_x = copy.deepcopy(vertexes)
vertexes_y = copy.deepcopy(vertexes)
vertexes_z = copy.deepcopy(vertexes)

# x, y, z좌표 각각 기준 정렬로 별개로 받아 람다식화로 새로운 배열에 담기
# 다른 행성 연결 비용 == 각 좌표차 최소값
vertexes_x.sort(key=lambda i: i[0])
vertexes_y.sort(key=lambda i: i[1])
vertexes_z.sort(key=lambda i: i[2])

edges = [[] for _ in range(count)]

for i in range(1, count):
    x1, y1, z1, i1 = vertexes_x[i - 1]
    x2, y2, z2, i2 = vertexes_x[i]
    weight = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    edges[i1].append((weight, i2))
    edges[i2].append((weight, i1))

    x1, y1, z1, i1 = vertexes_y[i - 1]
    x2, y2, z2, i2 = vertexes_y[i]
    weight = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    edges[i1].append((weight, i2))
    edges[i2].append((weight, i1))

    x1, y1, z1, i1 = vertexes_z[i - 1]
    x2, y2, z2, i2 = vertexes_z[i]
    weight = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    edges[i1].append((weight, i2))
    edges[i2].append((weight, i1))


print(prim(edges, 0))



