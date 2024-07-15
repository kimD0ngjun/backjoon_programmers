"""
https://www.acmicpc.net/problem/7576
"""
from collections import deque

# 입력 처리
M, N = map(int, input().split())

box = []
queue = deque()

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        if row[j] == 1:  # 익은 토마토가 있는 위치 큐 바로 할당
            queue.append((i, j))

    box.append(row)

# print(box)
# print("안 익은 토마토: " + str(count))

"""
익은 토마토: 1
안 익은 토마토: 0
빈 칸: -1

박스의 토마토가 전부 익을 때까지, 즉 count 가 0이 될 때까지
전형적인 bfs 문제 같은데
"""

# bfs 처리
dx = [1, -1, 0, 0]  # 상하
dy = [0, 0, -1, 1]  # 좌우


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))  # 큐에 새로운 토마토 위치 추가

# bfs 실행
bfs()

day = 0

for row in box:

    for i in row:
        if i == 0:  # 익지 않은 토마토가 있으면 -1 출력
            print(-1)
            # 바로 종료
            exit()
    else:
        # 그래프에서 가장 큰 값이 마지막으로 익은 토마토
        # 한 줄씩 최댓값을 day로 갱신하며 최댓값 찾기
        day = max(day, max(row))

# 처음 시작을 0이 아닌 1부터 했으므로 -1을 해야 날짜를 구할 수 있음
print(day - 1)
