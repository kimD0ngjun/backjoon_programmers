def solution(n):
    
    stack = []  # DFS용 스택
    all_count = 0
    
    for i in range(n):
        # 인덱스가 세로, 인덱스에 해당하는 값이 가로
        stack.append([i])

    while stack:
        current = stack.pop()

        # 1 입력했을 때 예외 처리
        if n == 1:
            all_count += 1
            break

        next_row = len(current)

        for i in range(n):
            # 최적화 조건
            if is_collision(current, next_row, i):
                continue

            new_path = current.copy()
            new_path.append(i)

            if len(new_path) == n:
                all_count += 1
            else:
                stack.append(new_path)
        
    return all_count

# 비교 함수
def is_collision(col, i, new_col):
    
    for k in range(i):
        if new_col == col[k] or abs(new_col - col[k]) == (i - k):
            return True
        
    return False