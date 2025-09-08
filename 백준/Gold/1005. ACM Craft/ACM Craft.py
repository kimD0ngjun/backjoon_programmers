"""
파이썬 50% 시간초과...
"""
from collections import deque

T = int(input())
answers = []

for _ in range(T):

    N, M = map(int, input().split())  # N : 노드 갯수, M : 간선 갯수
    graph = [[] for _ in range(N + 1)]
    entry_sizes = [0] * (N + 1)  # 진입값 사이즈
    times = [0] + list(map(int, input().split()))

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        entry_sizes[b] += 1  # 진입되는 간선 카운팅

    end = int(input())

    """
    칸 알고리즘 기반 위상정렬(BFS 차용) + DP
    """
    queue = deque() # 진입간선 0인 노드의 큐
    memo = [0] * (N + 1) # DP

    for i in range(1, N + 1):
        if entry_sizes[i] == 0:
            memo[i] = times[i]
            queue.append(i)  # 진입값 0인 애들부터 우선 큐 산입

    while queue:
        node = queue.popleft()

        for adj in graph[node]:
            entry_sizes[adj] -= 1  # 진입 간선 차감
            memo[adj] = max(memo[adj], memo[node] + times[adj])

            if entry_sizes[adj] == 0:
                queue.append(adj)

    answers.append(memo[end])

print(*answers, sep='\n')