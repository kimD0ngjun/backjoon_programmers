import sys
from collections import deque

sys_input = sys.stdin.readline

N, M = map(int, sys_input().split())

graph = [[] for _ in range(N + 1)]
queue = deque() # 진입간선 0인 노드의 큐
memo = [1] * (N + 1) # DP, 각 과목당 최소 할당 학기에서 최대 학기 찾아가는 메모이제이션

"""
무조건 마지막 과목은 N
"""
for _ in range(M):
    a, b = map(int, sys_input().split())
    graph[b].append(a) # 역방향 그래프

"""
1은 무조건 시작과목들 중 하나에 있고
N은 무조건 끝과목들 중 하나에 있음
"""
for i in range(1, N + 1):
    if len(graph[i]) == 0:
        continue

    # 역방향 그래프이므로 graph[i]는 이미 i에서 지나친 애들(계산 마무리된 애들)의 memo값들을 갖고옴
    memo[i] = max(memo[j] for j in graph[i]) + 1

print(*memo[1:])