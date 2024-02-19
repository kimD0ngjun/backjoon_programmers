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



# 프림 알고리즘(최대 신장 트리에서의 최소 가중치 간선 추출로 응용)
def prim(graph, start_vertex, end_vertex):
    connected = set()  # 간선 연결 정보
    heap = []  # 최소 힙

    min_weight = sys.maxsize
    heapq.heappush(heap, (-sys.maxsize, start_vertex))

    while heap:
        cur_weight, cur_adj_vertex = heapq.heappop(heap)

        if cur_adj_vertex not in connected:
            connected.add(cur_adj_vertex)
            
            if -cur_weight < min_weight:
                min_weight = -cur_weight

            if cur_adj_vertex == end_vertex:
                break

            for adj_vertex, weight in graph[cur_adj_vertex]:

                if adj_vertex not in connected:
                    heapq.heappush(heap, (-weight, adj_vertex))
    
        # exception
        if not heap:
            return 0
                    
    return min_weight


### 얘를 좀 변형시켜서 최대 신장 트리를 계산하면 되는 거 아닐까?
### 즉 최대 신장 트리로 응용시켜서 출력한 다음, start_vertex에서 end_vertex까지 갈 경로를 찾은 후,
### 그곳에서 최소 가중치 간선을 반환

### 아닌가? 그냥 최대신장트리 간선 가중치들 중에서 최소값을 반환하면 되나...?

# 입력 처리
graph_data = sys_input()
nodes, edges = map(int, graph_data.split())

vertex_data = sys_input()
start_vertex, end_vertex = map(int, vertex_data.split())

for i in range(edges):
    input_data = sys_input()
    vertex, adj_vertex, weight = map(int, input_data.split())

    make_graph(vertex, adj_vertex, weight)

print(prim(graph, start_vertex, end_vertex))
