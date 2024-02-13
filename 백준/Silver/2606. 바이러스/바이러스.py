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
    
    if value in graph:
        graph[value].append(key)
    else:
        graph[value] = [key]

# 반복문 DFS 함수
def dfs():
    discovered = set()
    stack.append(1)
    
    while stack:
        computer = stack.pop()
        
        temp = len(discovered)
        discovered.add(computer)
        if len(discovered) is not temp:
            
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
