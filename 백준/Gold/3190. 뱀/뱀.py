"""
https://www.acmicpc.net/problem/3190
"""
import sys
from collections import deque

N = int(input())  # 보드 크기(N * N)

maps = [[0] * N for _ in range(N)]

K = int(input())  # 사과 갯수

for _ in range(K):
    r, c = map(int, input().split())
    maps[r - 1][c - 1] = 2  # 사과 위치를 2로 표시

L = int(input())  # 방향 전환 횟수

turns = []
for _ in range(L):
    X, C = input().split()
    turns.append((int(X), C))

turns_queue = deque(turns)

"""
뱀의 초기 위치 : (0, 0)
뱀의 처음 길이 : 1
뱀의 처음 방향 : 오른쪽, 즉 (0, 1)

방향에 따른 맵 키값으로?

어느 방향 : 왼쪽 선택했을 떄의 방향(인덱스 0), 오른쪽 선택했을 때의 방향(인덱스 1)
(0, 1) : (-1, 0), (1, 0)
(-1, 0) : (0, -1), (0, 1)
(0, -1) : (1, 0), (-1, 0)
(1, 0) : (0, 1), (0, -1)
"""
turn_directions = {
    (0, 1): [(-1, 0), (1, 0)],
    (1, 0): [(0, 1), (0, -1)],
    (0, -1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, -1), (0, 1)]
}

direction = (0, 1)  # 초기 방향 오른쪽
time = 0
x, y = 0, 0  # 초기 위치
body_queue = deque([(x, y)])  # 뱀 위치
maps[x][y] = 1  # 뱀이 있는 위치

# print(maps)
# print(apples)
# print(turns_queue)
# print(body_queue)

while True:
    time += 1

    # 좌표 이동
    x += direction[0]
    y += direction[1]

    # 벽에 부딪히거나 자기 자신을 만난 경우
    if not (0 <= x < N and 0 <= y < N) or maps[x][y] == 1:
        print(time)
        break

    # 이동한 곳에 사과가 있는가?
    if maps[x][y] == 2:
        maps[x][y] = 1
        body_queue.appendleft((x, y))  # 대가리만 증가
    # 이동만 하는 경우
    else:
        maps[x][y] = 1
        body_queue.appendleft((x, y))
        tail_x, tail_y = body_queue.pop()
        maps[tail_x][tail_y] = 0  # 대가리 증가와 동시에 꼬리 수축

    # 방향 전환 케이스가 남아있으면서 시간대가 일치하다면
    if turns_queue and turns_queue[0][0] == time:
        _, C = turns_queue.popleft()
        if C == 'L':
            direction = turn_directions[direction][0]
        else:
            direction = turn_directions[direction][1]

"""
예상되는 놓친 예외
1. 시작 위치부터 사과가 있을 경우 -> 얘인 것 같은데?
2. 몸을 배배 꼬았는데, 꼬리 아직 수축 안했는데 머리가 들이미는 케이스 -> 얘는 아닌 것 같고
"""