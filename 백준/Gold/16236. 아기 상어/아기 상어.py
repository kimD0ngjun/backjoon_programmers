import sys
import copy
from collections import deque


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

"""
- 자신보다 작은 물고기는 지나치면서 없앰(길임과 동시에 아이템
- 자신이랑 같은 크기 물고기는 지나치기만 함(길이 될 수 있음)
- 자신보다 큰 물고기는 지나칠 수 없음(벽)

- 자신의 크기와 같은 마릿수의 물고기를 먹으면 크기 + 1
- 초기 크기는 2
- 동일 거리 기준으로 우선사항은 상단 -> 왼쪽
"""

# 아기 상어... 움직임 함수
# 크기, (시작x점, 시작y점), 업데이트용 임시 지도
def move(size, shark_start, temp_maps):
    # 시작점
    start_x, start_y = shark_start
    temp_maps[start_x][start_y] = -1

    dx = [1, -1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # 튜플 : (x, y, move_count)
    queue = deque()
    queue.append((start_x, start_y, 1))
    # move_count : 움직인 횟수 == 시간

    result = [] # 동일 거리 처리용 임시 리스트

    while queue:
        x, y, move_count = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 맵 벗어남
            if not (0 <= next_x < len(temp_maps) and 0 <= next_y < len(temp_maps[0])):
                continue

            # 자신보다 큰 물고기, 왔던길
            if temp_maps[next_x][next_y] > size or temp_maps[next_x][next_y] == -1:
                continue

            # 먹이 만남
            if 0 < temp_maps[next_x][next_y] < size:
                temp_maps[next_x][next_y] = -1
                result.append((next_x, next_y, move_count))
                continue

            # 왔던 길 표시
            temp_maps[next_x][next_y] = -1

            queue.append((next_x, next_y, move_count + 1))

    # 더 이상 이동할 곳이 없으면 move_count == 0을 반환한다
    if len(result) == 0:
        return -1, -1, 0

    # 최소 움직임 기준
    # 상단 기준
    # 왼쪽 기준
    # 최종 튜플
    min_tuple = min(result, key=lambda x: (x[2], x[0], x[1]))

    return min_tuple

def update_position(maps, temp_maps):
    # 아기 상어 위치
    for i in range(length):
        if 9 in temp_maps[i]:
            y = temp_maps[i].index(9)
            x = i

            maps[x][y] = 0
            return (x, y), maps

"""
입력 처리
"""

length = int(sys_input())
maps = [0] * length
shark_start = None

for i in range(length):
    maps[i] = [int(x) for x in sys_input().split()]

### 여기서부터 반복문 작업 시작이네
time = 0 # == move_count
size = 2 # 몸집
size_count = 0 # 몸집 업데이트 카운트

while True:
    # 몸집 성장 로직
    if size == size_count:
        size += 1
        size_count = 0

    temp_maps = copy.deepcopy(maps)
    shark_start, maps = update_position(maps, temp_maps)
    moved_x, moved_y, move_count = move(size, shark_start, temp_maps)

    if moved_x == -1:
        break

    time += move_count
    size_count += 1

    # 옮겨진 위치
    maps[moved_x][moved_y] = 9

print(time)