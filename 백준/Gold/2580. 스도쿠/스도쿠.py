sudoku = []
questions = []

for i in range(9):
    line = list(map(int, input().split()))
    sudoku.append(line)

    for j in range(9):
        if line[j] == 0:
            questions.append((i, j))

# def sol(x, y):
#     # 가로
#     for i in range(9):
#         if i == y:
#             continue
#
#         if sudoku[x][i] == sudoku[x][y]:
#             return False
#
#     # 세로
#     for i in range(9):
#         if i == x:
#             continue
#
#         if sudoku[i][y] == sudoku[x][y]:
#             return False
#
#     # 3 x 3
#     module_x = (x // 3) * 3
#     module_y = (y // 3) * 3
#
#     for i in range(module_x, module_x + 3):
#         for j in range(module_y, module_y + 3):
#             if i == x and j == y:
#                 continue
#
#             if sudoku[i][j] == sudoku[x][y]:
#                 return False
#
#     return True

# memo -> 실제 스도쿠 풀 때 칸에 후보군 메모하며 소거하던 거
row_memo = [set() for _ in range(9)]
column_memo = [set() for _ in range(9)]
module_memo = [set() for _ in range(9)]

# 초기 상태 설정
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            row_memo[i].add(sudoku[i][j])
            column_memo[j].add(sudoku[i][j])
            module_idx = (i // 3) * 3 + (j // 3)
            module_memo[module_idx].add(sudoku[i][j])

def backtrack(n):
    if n == len(questions):
        for line in sudoku:
            print(*line)

        exit()

    x, y = questions[n]
    module_idx = (x // 3) * 3 + (y // 3)
    for i in range(1, 10):

        if i not in row_memo[x] and i not in column_memo[y] and i not in module_memo[module_idx]:
            sudoku[x][y] = i
            row_memo[x].add(i)
            column_memo[y].add(i)
            module_memo[module_idx].add(i)

            if backtrack(n + 1):
                return True

            sudoku[x][y] = 0
            row_memo[x].remove(i)
            column_memo[y].remove(i)
            module_memo[module_idx].remove(i)

    return False

backtrack(0)