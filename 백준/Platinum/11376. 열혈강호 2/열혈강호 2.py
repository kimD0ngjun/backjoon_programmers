import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    graph[i] = line[1:]

match = [0] * (M + 1)

def dfs(node):
    if visited[node]:
        return False
    visited[node] = True

    for adj in graph[node]:
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = node
            return True

    return False

result = 0
for i in range(1, N + 1):
    for _ in range(2):
        visited = [False] * (N + 1)
        if dfs(i):
            result += 1

print(result)