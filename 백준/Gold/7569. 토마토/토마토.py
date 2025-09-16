from collections import deque

M, N, H = map(int, input().split())

box = [[] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

for h in range(H):
    for i in range(N):
        line = list(map(int, input().split()))

        for j in range(M):
            if line[j] == 1:
                queue.append((i, j, h))

        box[h].append(line)

# print(box)

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = box[z][x][y] + 1
            queue.append((nx, ny, nz))

day = 0

for floor in box:
    for i in floor:
        for j in i:
            if j == 0:
                print(-1)
                exit()
            else:
                day = max(day, j)

print(day - 1)