import sys
import heapq


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# 프림 알고리즘
def prim(graph):
    connected = set()
    heap = []

    heapq.heappush(heap, (0, 0))

    min_sum_weight = 0

    while heap:
        cur_weight, cur_vertex = heapq.heappop(heap)

        if cur_vertex not in connected:
            connected.add(cur_vertex)
            min_sum_weight += cur_weight

            for adj_vertex, weight in enumerate(graph[cur_vertex]):
                if weight != 0 and adj_vertex not in connected:
                    heapq.heappush(heap, (weight, adj_vertex))

    return min_sum_weight


# 입력 처리
nodes = int(sys_input())

graph = [None] * nodes

for i in range(nodes):
    input_data = sys_input()
    weight_list = [int(x) for x in input_data.strip().split()]
    graph[i] = weight_list

print(prim(graph))