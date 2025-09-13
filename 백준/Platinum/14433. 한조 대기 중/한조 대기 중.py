import sys
input = sys.stdin.readline

N, M, K1, K2 = map(int, input().split())
team = [[] for _ in range(N + 1)]
opponent = [[] for _ in range(N + 1)]
team_match = [-1] * (M + 1)
opponent_match = [-1] * (M + 1)

for _ in range(K1):
    i, j = map(int, input().split())
    team[i].append(j)

for _ in range(K2):
    i, j = map(int, input().split())
    opponent[i].append(j)

def dfs(node, graph, match):
    if visited[node]:
        return False

    visited[node] = True

    for adj in graph[node]:
        if match[adj] == -1 or dfs(match[adj], graph, match):
            match[adj] = node
            return True

    return False

team_result = 0
for i in range(1, N + 1):
    visited  = [False] * (N + 1)
    if dfs(i, team, team_match): team_result += 1

opponent_result = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    if dfs(i, opponent, opponent_match): opponent_result += 1

print("네 다음 힐딱이") if team_result < opponent_result else print("그만 알아보자")