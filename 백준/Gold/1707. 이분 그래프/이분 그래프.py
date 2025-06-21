"""
이분 그래프 : 정점 색 번갈아 색칠할 때, 전부 채울 수 있는가?
"""
import sys
sys.setrecursionlimit(100_000)


def dfs(vertex, color):
    colors[vertex] = color

    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return True

        if colors[neighbor] == 0:
            if dfs(neighbor, -color):
                return True

    return False


def input():
    return sys.stdin.readline().strip()


answers = []
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    colors = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    flag = True

    for i in range(1, V + 1):
        if colors[i] == 0:
            if dfs(i, 1):
                flag = False
                break

    answers.append("YES" if flag else "NO")

for answer in answers:
    print(answer)
