"""
https://school.programmers.co.kr/learn/courses/30/lessons/86052
"""


def solution(grid):
    answer = []

    column = len(grid[0])
    row = len(grid)

    dp = [[[False, False, False, False] for _ in range(column)] for _ in range(row)]

    for i in range(row):
        for j in range(column):
            for k in range(4):
                if not dp[i][j][k]:
                    cycle = bfs(i, j, k, dp, grid)

                    if cycle > 0:
                        answer.append(cycle)

    return sorted(answer)


# bfs(파라미터: 시작 지점 및 지점으로부터 나아가려는 방향, dp 배열, 그리드)
def bfs(row_index, column_index, direction_index, dp, grid):
    length = 0

    # 방향을 나타내는 배열
    # 남, 동, 북, 서
    # 반시계 방향으로 0 1 2 3
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while True:
        # 해당 dp가 방문 기록이 있다면 그게 곧 사이클이라는 뜻
        if dp[row_index][column_index][direction_index]:
            break

        # 현재 위치와 방향 기록
        dp[row_index][column_index][direction_index] = True
        length += 1

        # 다음 위치로 이동
        # 영역 넘김 순환 모듈러 처리
        row_index = (row_index + dy[direction_index]) % len(dp)
        column_index = (column_index + dx[direction_index]) % len(dp[0])

        # 방향 변경
        if grid[row_index][column_index] == "L":
            direction_index = (direction_index + 3) % 4
        elif grid[row_index][column_index] == "R":
            direction_index = (direction_index + 1) % 4

    return length


# print(solution(["SL","LR"]))
# print(solution(["S"]))
# print(solution(["R","R"]))
