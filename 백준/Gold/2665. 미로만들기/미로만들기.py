import heapq
from collections import deque

n = int(input().strip())
maze = [list(map(int, input().strip())) for _ in range(n)]

# dx = [1, -1, 0, 0]  # 아래, 위
# dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽
#
# queue = deque()
# queue.append((0, 0, 1))  # x, y, count
# visited = [[False] * n for _ in range(n)]
# visited[0][0] = True
#
# while queue:
#     x, y, count = queue.popleft()
#
#     if x == n - 1 and y == n - 1:
#         print(count)
#         break
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < n:
#             if maze[nx][ny] == 1 and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny, count + 1))


"""
방을 부순다
방이 아니라 경로라 생각하면 경로 가중치가 0이거나 1인 케이스뿐
그 중의 최소 합산 가중치 -> 다익스트라
격자 탐색 -> BFS

0-1 BFS
1. 간선의 가중치는 반드시 0 또는 1이어야 함
2. Deque 자료구조를 사용함
3. 시간 복잡도는 O(V + E)
4. 0-1 BFS 문제는 다익스트라로도 해결 가능
5. 탐색 시 각 노드마다 최소 비용을 저장할 int 배열 필요
"""

# 다익스트라 풀이(격자형 하드코딩)
def dijkstra(maze):
    INF = float('inf')
    min_costs = [[INF] * n for _ in range(n)]
    min_costs[0][0] = 0 # 시작 비용
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = [(0, 0, 0)] # cost, x, y

    while queue:
        cost, x, y = heapq.heappop(queue)

        if min_costs[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + (1 if maze[nx][ny] == 0 else 0)
                if next_cost < min_costs[nx][ny]:
                    min_costs[nx][ny] = next_cost
                    heapq.heappush(queue, (next_cost, nx, ny))

    return min_costs[n - 1][n - 1]

print(dijkstra(maze))