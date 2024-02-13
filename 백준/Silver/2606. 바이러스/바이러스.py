# 그래프 문제는 기본적으로 별 얘기 없으면 양방향 그래프

import sys

graph = {}
stack = []

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
def dfs():
    discovered = []
    stack.append(1)
    
    while stack:
        computer = stack.pop()
        
        if computer not in discovered:
            discovered.append(computer)
            
            neighbors = graph.get(computer)
            if neighbors is not None:
                for neighbor in neighbors:
                    stack.append(neighbor)
    
    return len(discovered) - 1

# 입력
count = int(sys_input())
pair = int(sys_input())

for _ in range(pair):
    input_data = sys_input()
    key, value = map(int, input_data.split())
    
    make_graph(key, value)

# 출력
print(dfs())
