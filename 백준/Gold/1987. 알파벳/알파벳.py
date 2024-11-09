R, C = map(int, input().split())

board = []

for _ in range(R):
    board.append(list(input().strip()))


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
visited_init = [False for x in range(26)]
memo = {}


def backtrack(x, y, path, visited):
    global result

    state = (x, y, tuple(visited))  # tuple key

    if state in memo:
        return memo[state]

    result = max(result, path)  # 경로 길이 갱신
    alphabet = board[x][y]
    visited[ord(alphabet) - 65] = True

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if not (0 <= next_x < R and 0 <= next_y < C):
            continue

        next_alphabet = board[next_x][next_y]

        if visited[ord(next_alphabet) - 65] is False:
            backtrack(next_x, next_y, path + 1, visited)

    visited[ord(alphabet) - 65] = False  # backtracking
    memo[state] = result  # memoization
    
    return memo[state]


backtrack(0, 0, 1, visited_init)
print(result)
