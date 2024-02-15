import sys
from queue import deque

# 지도 선언
maps = []

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()
    
# BFS 함수 선언
def bfs(start_x, start_y, maps):
    queue = deque()
    
    dx = [1, -1, 0, 0] # 상하
    dy = [0, 0, -1, 1] # 좌우
    
    # 튜플 : (x, y)
    # 상단은 0, start_y
    # 우단은 start_x, len(maps) - 1
    # 하단은 len(maps) - 1, start_y
    # 좌단은 start_x, 0
    queue.append((start_x, start_y))
    maps[start_x][start_y] = 0  # 시작점 방문 표시

    width = 0 # 면적 선언
    
    while queue:
        x, y = queue.popleft()
        width += 1
        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            # 백트랙킹 조건 : 맵 벗어나기, 벽 도달
            if not (0 <= next_x < len(maps) and 0 <= next_y < len(maps[0])):
                continue
            
            if maps[next_x][next_y] == 0:
                continue
                
            # 방문 처리
            if maps[next_x][next_y] == 1:
                # 방문했으면 다시 벽 처리
                maps[next_x][next_y] = 0
                queue.append((next_x, next_y))

    # 탐색 마무리 후, 최종 너비와 탐색 완료 업뎃된 맵을 함께 반환
    return width, maps

# 면적 탐색 함수 선언
def calculate_width(initial_maps):   
    # 겉 테두리를 한바퀴 뺑 돌아야 할 듯...?
    maps = initial_maps
    widths = []
    
    # 상단면
    for i in range(len(maps)):
        for j in range(len(maps)):
            # 집 발견하면 시작
            if maps[i][j] == 1:
                width, update_maps = bfs(i, j, maps)
            
                widths.append(width)
                maps = update_maps
    
    return widths

# 입력 처리 및 지도 생성, 계산
length = int(sys_input())

for _ in range(length):
    input_line = sys_input()
    column = [int(num) for num in input_line]
    
    maps.append(column)

widths = calculate_width(maps)
sorted_widths = sorted(widths)

# 출력 처리
print(len(sorted_widths))

for i in range(len(sorted_widths)):
    print(sorted_widths[i])
    