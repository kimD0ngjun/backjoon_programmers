# 알고리즘 감각 다시 살리기...
from collections import deque

maze = []
N, M = map(int, input().split())

for _ in range(N):
    line = list(map(int, input().strip()))
    maze.append(line)

# print(maze)


def dfs(N, M, maze):
    queue = deque()
    dx = [1, -1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # 튜플 : (x, y, distance)
    queue.append((0, 0, 1))

    while queue:
        x, y, distances = queue.popleft()

        # end
        if x == N - 1 and y == M - 1:
            return distances

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if not (0 <= next_x < N and 0 <= next_y < M):
                continue

            if maze[next_x][next_y] == 0:
                continue

            # 방문 처리
            if maze[next_x][next_y] == 1:
                # 방문했으면 다시 벽 처리
                maze[next_x][next_y] = 0
                queue.append((next_x, next_y, distances + 1))


print(dfs(N, M, maze))