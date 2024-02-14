stack = []  # DFS용 스택
all_count = 0

# 비교 함수
def is_collision(col, i, new_col):
    for k in range(i):
        if new_col == col[k] or abs(new_col - col[k]) == (i - k):
            return True
    return False

# 입력 처리
n = int(input())

for i in range(n):
    stack.append([i])  # 단일 배열로 변경

while stack:
    current = stack.pop()

    # 1 입력했을 때 예외 처리
    if n == 1:
        all_count += 1
        break

    next_row = len(current)

    for i in range(n):
        if is_collision(current, next_row, i):
            continue

        new_path = current.copy()
        new_path.append(i)

        if len(new_path) == n:
            all_count += 1
        else:
            stack.append(new_path)

print(all_count)
