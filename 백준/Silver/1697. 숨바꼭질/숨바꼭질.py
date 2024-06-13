"""
https://www.acmicpc.net/problem/1697
"""
from collections import deque

# 입력 처리
N, K = map(int, input().split())


# BFS(좌표, 소요 시간)
queue = deque()
queue.append((N, 0))

# 방문 기록 및 초기 위치 방문 처리
visited = [False] * 100_001
visited[N] = True

while queue:
    current = queue.popleft()
    position = current[0]
    time = current[1]

    # 위치 도달시 반복문 파괴
    if position == K:
        print(time)
        break

    # 1초 후에 X - 1
    # 1초 후에 X + 1
    # 1초 후에 2 * X
    moves = [position - 1, position + 1, position * 2]

    for move in moves:
        if 0 <= move <= 100_000 and not visited[move]:
            visited[move] = True
            queue.append((move, time + 1))