from collections import deque

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

answers = []

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    count = 0

    for i in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    # print(graph)
    for i in range(M):
        for j in range(N):
            # print(f"인덱스 i: {i}, 인덱스 j: {j}")
            if graph[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                graph[i][j] = 0  # 방문 처리

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if not (0 <= nx < M and 0 <= ny < N):
                            continue

                        if graph[nx][ny] == 0:
                            continue

                        graph[nx][ny] = 0
                        queue.append((nx, ny))

                count += 1

    answers.append(count)

print(*answers, sep="\n")