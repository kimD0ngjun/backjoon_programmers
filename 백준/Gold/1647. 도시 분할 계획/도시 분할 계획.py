import sys
import heapq
from collections import defaultdict

graph = defaultdict(dict)


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# 그래프 생성 함수
def make_graph(key, value, weight):
    if key in graph:
        graph[key].append((value, weight))
    else:
        graph[key] = [(value, weight)]

    if value in graph:
        graph[value].append((key, weight))
    else:
        graph[value] = [(key, weight)]


# 프림 알고리즘
def prim(graph):
    connected = set()
    heap = []

    heapq.heappush(heap, (0, 1))

    min_sum_weight = 0
    max_weight = 0

    while heap:
        cur_weight, cur_vertex = heapq.heappop(heap)

        if cur_vertex not in connected:
            connected.add(cur_vertex)
            min_sum_weight += cur_weight

            # MST내에서의 최대 가중치 간선 구하기 추가
            if max_weight < cur_weight:
                max_weight = cur_weight

            for adj_vertex, weight in graph[cur_vertex]:
                if adj_vertex not in connected:
                    heapq.heappush(heap, (weight, adj_vertex))

    return min_sum_weight - max_weight


# 입력 처리
graph_data = sys_input()
nodes, edges = map(int, graph_data.split())

for i in range(edges):
    input_data = sys_input()
    vertex, adj_vertex, weight = map(int, input_data.split())

    make_graph(vertex, adj_vertex, weight)

print(prim(graph))
