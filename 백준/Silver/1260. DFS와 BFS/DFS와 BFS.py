import sys
from collections import deque

graph = {}
stack = []
queue = deque()

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 그래프 생성 함수
def make_graph(key, value):
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]
    
    # 양방향 고려
    if value in graph:
        graph[value].append(key)
    else:
        graph[value] = [key]
        
# 반복문 DFS 함수
def dfs(start):
    discovered = []
    stack.append(start)
    result = []
    
    while stack:
        current = stack.pop()
        
        if current not in discovered:
            discovered.append(current)
            result.append(current)
            
            neighbors = graph.get(current)
            if neighbors is not None:
                neighbors.sort(reverse=True)
                for neighbor in neighbors:
                    stack.append(neighbor)
    
    print(*result)

# 반복문 BFS 함수
def bfs(start):
    discovered = []
    queue.append(start)
    result = []
    
    while queue:
        current = queue.popleft()
        
        if current not in discovered:
            discovered.append(current)
            result.append(current)
            
            neighbors = graph.get(current)
            if neighbors is not None:
                neighbors.sort()
                for neighbor in neighbors:
                    queue.append(neighbor)
    
    print(*result)

# 입력 처리
input_data = sys_input()
vertexs, edges, start = map(int, input_data.split())

for _ in range(edges):
    input_data = sys_input()
    key, value = map(int, input_data.split())
    
    make_graph(key, value)

dfs(start)
bfs(start)