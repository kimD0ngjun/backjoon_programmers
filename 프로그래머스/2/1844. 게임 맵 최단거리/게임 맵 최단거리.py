from queue import deque

def solution(maps):
    # 코드에서의 좌표 개념 : (상하, 좌우)
    # 이중 리스트에서의 상하좌우이므로 상하는 겉 리스트의 인덱스, 좌우는 내부 리스트의 인덱스
    
    dx = [1, -1, 0, 0] # 상하
    dy = [0, 0, -1, 1] # 좌우
    
    # 길찾기는 BFS가 맞는듯? DFS는 백트랙킹 생각하기가 넘 빡세다...
    # 좌표는 추출이 쉽게 튜플의 형식으로 생각할 것
    
    # 벽 + 왔던 길 : 0, 길 : 1
    # 튜플 : (x, y, distance)
    queue = deque()
    queue.append((0, 0, 1))
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 팝했을 때 종점에 도착했다면
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return distance
        
        # 네 방향이므로
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
                
                queue.append((next_x, next_y, distance + 1))
    
    # 큐가 비워질 때까지 종점의 좌표를 팝하지 못하면 그건 길이 막혔다는 뜻
    return -1