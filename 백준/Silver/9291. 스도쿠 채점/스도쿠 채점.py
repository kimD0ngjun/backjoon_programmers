"""
https://www.acmicpc.net/problem/9291
"""


# 행 검증
def check_row(sudoku):
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            return False

    return True


# 열 검증
def check_column(sudoku):
    for i in range(9):

        unit_column = []
        for j in range(9):
            unit_column.append(sudoku[j][i])

        if len(set(unit_column)) != 9:
            return False

    return True


# 모듈 검증
def check_module(sudoku):
    # 모듈 인덱스
    module_indexes = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    for module_index in module_indexes:
        unit_module = []
        x, y = module_index

        for i in range(x, x + 3):
            for j in range(y, y + 3):
                unit_module.append(sudoku[i][j])

        if len(set(unit_module)) != 9:
            return False

    return True


# 입력
N = int(input())

for i in range(N):
    unit_sudoku = []

    for _ in range(9):
        row = list(map(int, input().split()))
        unit_sudoku.append(row)

    # 출력
    if check_row(unit_sudoku) and check_column(unit_sudoku) and check_module(unit_sudoku):
        print(f"Case {i + 1}: CORRECT")
    else:
        print(f"Case {i + 1}: INCORRECT")

    if i < N - 1:
        input()
