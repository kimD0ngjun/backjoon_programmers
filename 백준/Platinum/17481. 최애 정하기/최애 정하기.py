import sys

input = sys.stdin.readline

N, M = map(int, input().split())
idol = []

for _ in range(M):
    idol.append(input().strip())

idol_index = {name: idx+1 for idx, name in enumerate(idol)}

graph = [[] for _ in range(N + 1)]
match = [-1] * (M + 1)

for i in range(1, N + 1):
    line = input().split()
    for el in line[1:]:
        graph[i].append(idol_index[el])

def dfs(node, id):
    if visited[node] == id:
        return False

    visited[node] = id

    for adj in graph[node]:
        if match[adj] == -1 or dfs(match[adj], id):
            match[adj] = node
            return True

    return False

result = 0
visited = [0] * (N + 1)
visit_id = 1

for i in range(1, N + 1):
    if dfs(i, visit_id):
        result += 1
    visit_id += 1

print("YES" if result == N else f"NO\n{result}")