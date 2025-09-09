"""
위상 정렬(topological sorting)은 유향 그래프의 꼭짓점들(vertex)을 변의 방향을 거스르지 않도록 나열하는 것
사이클 판별 알고리즘으로도 활용할 수 있을듯. 위상 정렬 자체가 DAG(사이클 없는 방향 그래프)에서만 적용 가능하므

결국 간선을 중심으로, '위상 정렬'의 결과로 나온 간선들 중 어느 것을 뽑아도 노드 간 선후 관계가 준수될 것
팬인 사이즈가 0인 애들부터 하나씩 그래프에서 삭제해나가기?

자기 자신을 가리키는 변이 없는 꼭짓점을 찾음.
찾은 꼭짓점을 출력하고 출력한 꼭짓점과 그 꼭짓점에서 출발하는 변을 삭제
아직 그래프에 꼭짓점이 남아있으면 단계 1로 돌아가고, 아니면 알고리즘을 종료시킨다.
"""
import sys
from collections import deque

sys_input = sys.stdin.readline

N = int(sys_input())

graph = [[] for _ in range(N + 1)]
entry_sizes = [0] * (N + 1)  # 진입값 사이즈
times = [0]
queue = deque() # 진입간선 0인 노드의 큐
memo = [0] * (N + 1) # DP

for i in range(1, N + 1):
    line = list(map(int, sys_input().split()))
    times.append(line[0]) # 작업 시간 할당

    if line[1] == 0:
        memo[i] = line[0]
        queue.append(i)
        continue

    for j in range(2, len(line)):
        graph[line[j]].append(i)
        entry_sizes[i] += 1

# print(f"그래프: {graph}")
# print(f"타임: {times}")
# print(f"팬인 사이즈: {entry_sizes}")

"""
칸 알고리즘 기반 위상정렬(BFS 차용) + DP
"""
# answer = []

while queue:
    node = queue.popleft()
    # answer.append(node)

    for adj in graph[node]:
        entry_sizes[adj] -= 1  # 진입 간선 차감
        memo[adj] = max(memo[adj], memo[node] + times[adj])

        if entry_sizes[adj] == 0:
            queue.append(adj)

# print(answer)
# print(memo)

print(max(memo))