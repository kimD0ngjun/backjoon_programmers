from collections import deque

board = {}

N, M = map(int, input().split())

for _ in range(N):
    a, b = map(int, input().split())
    board[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    board[a] = b

# print(board)

queue = deque()
queue.append((1, 0)) # start, count
flag = True
visited = set()

while queue and flag:
    square, count = queue.popleft()

    for i in range(1, 7):
        next_square = square + i

        while next_square in board:
            next_square = board[next_square]

        if next_square == 100:
            print(count + 1)
            flag = False
            break
        #
        # if next_square in board:
        #     queue.append((board[next_square], count + 1))

        if not next_square in visited:
            visited.add(next_square)
            queue.append((next_square, count + 1))