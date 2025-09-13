import sys
input = sys.stdin.readline

N = int(input().strip())
sharks = [tuple(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        # 상어 i가 상어 j보다 능력치가 높을 경우
        if sharks[i][0] >= sharks[j][0] and sharks[i][1] >= sharks[j][1] and sharks[i][2] >= sharks[j][2]:
            # 단 능력치가 모두 같으면 i < j 인 경우에만
            if sharks[i] == sharks[j] and i > j:
                continue
            graph[i].append(j)

match = [-1] * N # 상어 j 기준 사냥 매핑

def dfs(node):
    for adj in graph[node]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = node
            return True
    return False

result = 0
for i in range(N):
    # 상어는 최대 두 마리까지 먹을 수 있음
    # 열혈강호 2 pypy3 버전이랑 비슷한 거 같은데 이거
    for _ in range(2):
        visited = [False] * N
        if dfs(i):
            result += 1

# 전체 수 - 사냥당한 횟수 = 살아남는 상어 수
print(N - result)