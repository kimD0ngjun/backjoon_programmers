"""
https://www.acmicpc.net/problem/1520
"""
import copy

M, N = map(int, input().split())

maps = []

for _ in range(M):
    rows = list(map(int, input().split()))
    maps.append(rows)

# print(maps)

"""
start : 0, 0

-> 모든 경우가 끝날 때까지 계에에에속 기다려야함
-> 예를 들면 나머지는 30초 내로 전부 끝냈는데 꼴찌가 1시간 걸리는 경우..?
-> 길 잘못 들어서면 망

bfs? 
-> 잔산 수색하는 형식이라 메모이제이션 활용도 낮음  

dfs?
-> 그나마 bfs보다는 메모이제이션 나을 거 같은데
-> 만약 특정 길 막혔다는 건, 그쪽 향하는 길로 다신 안 가게 하면 되니까 근데 그걸 어케 기억시킬까
-> 갈림길이 나오는 케이스라면 어떻게 처리할까(갈림길부터 출발하도록 처리하기?)
-> 갈림길부터 시작하게 하려면 재귀함수로 구현하기...?
"""

count = 0

# 경로 계산 x : -1
memo = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 기억용
# visited = [[False] * N for _ in range(M)]

def dfs(x, y):
    global count

    # 탈출 조건
    # 가장 밑바닥에서 1 반환시켜서 개수 계속 합산시키기
    if x == M - 1 and y == N - 1:
        return 1

    # 메모이제이션 활용
    # 이미 일전에 계산된 경로 카운트가 존재하면 그걸 바로 반환
    if memo[x][y] != -1:
        return memo[x][y]

    # 여기까지 왔으면 경로 계산을 해야되는데
    # 아직 경로 계산 시작이 안 된 상태이므로 초기화
    memo[x][y] = 0

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 맵 밖으로 벗어나는 경우 무시
        if not (0 <= next_x < M and 0 <= next_y < N):
            continue

        # 자신의 값보다 크거나 같으면 무시
        if maps[x][y] <= maps[next_x][next_y]:
            continue

        # 다음 위치로 이동
        # 이동하면서 경로 수 누적 받아와야함(반복문 분기로 갈리는 4가지 케이스 재귀)
        memo[x][y] += dfs(next_x, next_y)

    # 해당 지점의 경로 카운팅된 거 반환
    return memo[x][y]


print(dfs(0, 0))

