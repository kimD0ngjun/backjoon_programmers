# 현재까지 가장 근접한 정답

"""
https://www.acmicpc.net/problem/2580
"""
import sys

"""
시간초과난 풀이 접근
- 메모이제이션과 백트랙킹 (+ 모듈 bfs) : 1퍼 펑
- exit() 강제 호출 전 : 13퍼 펑
- exit() 강제 호출 : 81퍼 펑
"""

# 입력
sudoku = []
blanks = []

# 빈칸은 0 입력
# blanks가 빈칸 위치 추적 리스트
for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    sudoku.append(row)

    for j in range(9):
        if row[j] == 0:
            blanks.append((i, j))

# 메모이제이션...?
row_memo = [set() for _ in range(9)]
column_memo = [set() for _ in range(9)]
module_memo = [set() for _ in range(9)]

# 초기 상태 설정
for r in range(9):
    for c in range(9):
        num = sudoku[r][c]
        if num != 0:
            row_memo[r].add(num)
            column_memo[c].add(num)
            module_index = (r // 3) * 3 + (c // 3)
            module_memo[module_index].add(num)


# # 행의 단위 리스트 숫자 가능성 체크
# def row(x, n):
#     for i in range(9):
#         # n이 x의 행에 이미 갖고 있는가?
#         if n == sudoku[x][i]:
#             return False
#
#     return True
#
#
# # print(row(0, 1))
#
# # 열의 숫자 가능성 체크
# def column(y, n):
#     for i in range(9):
#         # n이 y의 열에 이미 갖고 있는가?
#         if n == sudoku[i][y]:
#             return False
#
#     return True
#
#
# # # 브루트 포스 대신 단순 반복문
# # 모듈의 숫자 가능성 체크
# def module(x, y, n):
#     range_x = x // 3 * 3
#     range_y = y // 3 * 3
#
#     for i in range(3):
#         for j in range(3):
#
#             # n이 모듈 내에 이미 갖고 있는가?
#             if n == sudoku[range_x + i][range_y + j]:
#                 return False
#
#     return True


# 풀이 시작
def solve(n):
    # 모든 빈칸을 다 훑었으면
    if len(blanks) == n:
        for line in sudoku:
            print(' '.join(map(str, line)))

        exit()

    x, y = blanks[n]
    box_idx = (x // 3) * 3 + (y // 3)

    for num in range(1, 10):
        # 반복문 대신 집합을 쓴다면...?
        if num not in row_memo[x] and num not in column_memo[y] and num not in module_memo[box_idx]:
            sudoku[x][y] = num
            row_memo[x].add(num)
            column_memo[y].add(num)
            module_memo[box_idx].add(num)

            if solve(n + 1):
                return True

            sudoku[x][y] = 0
            row_memo[x].remove(num)
            column_memo[y].remove(num)
            module_memo[box_idx].remove(num)

    return False


solve(0)
