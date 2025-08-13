import heapq


def prim(graph, start_vertex, v):
    mst_graph = {i: [] for i in range(1, v + 1)}

    connected = set()
    queue = []
    connected_vertex = 1
    heapq.heappush(queue, (0, start_vertex, connected_vertex))

    # 최소 가중치
    min_sum_weight = 0

    while queue:
        cur_weight, cur_adj_vertex, cur_connected_vertex = heapq.heappop(queue)
        if cur_adj_vertex not in connected:
            connected.add(cur_adj_vertex)
            min_sum_weight += cur_weight

            if cur_connected_vertex != cur_adj_vertex:
                mst_graph[cur_connected_vertex].append((cur_adj_vertex, cur_weight))
                mst_graph[cur_adj_vertex].append((cur_connected_vertex, cur_weight))

            for adj_vertex, weight in graph[cur_adj_vertex]:
                if adj_vertex not in connected:
                    heapq.heappush(queue, (weight, adj_vertex, cur_adj_vertex))

    return min_sum_weight, mst_graph

graph = {}

V, E = map(int, input().split())

for _ in range(E):
    A, B, C = map(int, input().split())

    if A in graph:
        graph[A].append((B, C))
    else:
        graph[A] = [(B, C)]

    if B in graph:
        graph[B].append((A, C))
    else:
        graph[B] = [(A, C)]

msw, _ = prim(graph, 1, V)
print(msw)