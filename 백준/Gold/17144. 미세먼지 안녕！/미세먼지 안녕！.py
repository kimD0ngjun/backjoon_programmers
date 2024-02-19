import sys
from collections import deque


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 먼지 함수
def diffusion(update, graph, cleaner_position):
    dx = [1, -1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    for x, y in update:
        dust = graph[x][y][0]
        spread_dust = dust // 5
        # 인덱스 1에 덧붙여짐
        graph[x][y][1] = spread_dust
        direction = 0

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

             # 일단 벽 너머에 도달하였는가?
            if not 0 <= next_x <= row - 1 or not 0 <= next_y <= column - 1:
                continue

            # 공기청정기에 닿았는가?
            if (next_x == cleaner_position and next_y == 0) or (next_x == cleaner_position + 1 and next_y == 0):
                continue

            # 퍼지는 방향 확인
            direction += 1

            # 퍼지는 방향에 대허 퍼진 먼지 증감(인덱스 2에 덧붙여짐)
            graph[next_x][next_y][2] += spread_dust

        # 현재 자리 우선 먼지 업데이트
        graph[x][y][0] -= (graph[x][y][1] * direction)

# 외부 먼지 더하기
# 요거 청정 작업( 0 -> 2 ) 처리한 다음에 재활용하기
def accept_dust(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            # 외부 먼지 더하기
            graph[i][j][0] += graph[i][j][2]

            graph[i][j][1] = 0
            graph[i][j][2] = 0

# 클리너 함수
def up_cleaner(graph, cleaner_position):

    for i in range(cleaner_position + 1):
        for j in range(len(graph[i])):
            # 하면
            if i == cleaner_position and 0 < j < len(graph[i]) - 1:
                graph[i][j + 1][1] = graph[i][j][0]

            # 우면
            if i != 0 and j == len(graph[i]) - 1:
                graph[i - 1][j][1] = graph[i][j][0]

            # 상면
            if i == 0 and j != 0:
                graph[i][j - 1][1] = graph[i][j][0]
            #
            # 좌면
            if j == 0 and i != cleaner_position and i + 1 != cleaner_position:
                graph[i + 1][j][1] = graph[i][j][0]

def down_cleaner(graph, cleaner_position):
    down = cleaner_position + 1

    for i in range(down, len(graph)):
        for j in range(len(graph[i])):
            # 상면
            if i == down and j != 0 and j != len(graph[i]) - 1:
                graph[i][j + 1][1] = graph[i][j][0]

            # 우면
            if i != len(graph) - 1 and j == len(graph[i]) - 1:
                graph[i + 1][j][1] = graph[i][j][0]
            #
            # 하면
            if i == len(graph) - 1 and 0 != j:
                graph[i][j - 1][1] = graph[i][j][0]

            #
            # 좌면
            if j == 0 and i != down and i + 1 != down:
                graph[i - 1][j][1] = graph[i][j][0]

# 정리
def rearrange(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if i == 0 or i == len(graph) - 1 or j == len(graph[0]) - 1:
                graph[i][j][0] = graph[i][j][1]
                graph[i][j][1] = 0

            if j == 0 and 0 < i < len(graph) - 1 and graph[i][j][0] != -1:
                graph[i][j][0] = graph[i][j][1]
                graph[i][j][1] = 0

            if (i == cleaner_position and graph[i][j][0] != -1 and j != len(graph[0]) - 1) or (i == cleaner_position + 1 and graph[i][j][0] != -1 and j != len(graph[0]) - 1):
                graph[i][j][0] = graph[i][j][1]
                graph[i][j][1] = 0

def sum_graph(graph):
    total_sum = 0
    for inner_list in graph:
        for sub_inner_list in inner_list:
            total_sum += sub_inner_list[0]
    return total_sum + 2

"""
입력 및 출력 처리
"""

row, column, time =  map(int, sys_input().split())

graph = [0] * row
cleaner_position = 0

for i in range(row):
    # 인덱스 0: 기존 먼지, 인덱스 1: 기존 먼지 // 5, 인덱스 2: 외부 먼지
    graph[i] = [[int(x), 0, 0] for x in sys_input().split()]

    if -1 in graph[i][0]:
        # 두번 검색되므로 마지막 것이 업뎃
        cleaner_position = i - 1

for _ in range(time):
    update = []

    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y][0] != 0 and graph[x][y][0] != -1:
                update.append((x, y))

    diffusion(update, graph, cleaner_position)
    accept_dust(graph)
    # 공기청정기
    up_cleaner(graph, cleaner_position)
    down_cleaner(graph, cleaner_position)
    rearrange(graph)

print(sum_graph(graph))