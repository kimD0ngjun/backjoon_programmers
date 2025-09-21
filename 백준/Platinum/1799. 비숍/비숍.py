"""
N비숍 문제 + 놓을 수 없는 칸
비숍이 한 대각선 라인을 차지하면, 그 대각선 라인은 열값과 상관없이 전멸
근데 퀸과 다르게 행도 고려해야 됨, 같은 행에는 가능하다면 전부 배치 가능하므로
"""
N = int(input())
black = []
white = []

for i in range(N):
    line = list(map(int, input().split()))

    for j in range(N):
        if line[j] == 1:
            if (i + j) % 2 == 0:
                black.append((i, j))
            else:
                white.append((i, j))

left = 0 # 왼쪽 아래 대각선
right = 0 # 오른쪽 아래 대각선
black_answer = 0
white_answer = 0

"""
현재 구조는 흑백 같이 해서 곱연산 탐색
흑백을 아예 따로 두고 합연산을 하면 탐색이 덜 할듯?
"""
def backtrack_black(el, count):
    global left, right, black_answer

    if el == len(black):
        black_answer = max(black_answer, count)
        return

    r, c = black[el]

    if (left & (1 << r + c)) == 0 and (right & (1 << r - c + (N - 1))) == 0:
        left = left | (1 << r + c)
        right = right | (1 << r - c + (N - 1))
        backtrack_black(el + 1, count + 1)
        left = left & ~(1 << r + c)
        right = right & ~(1 << r - c + (N - 1))

    backtrack_black(el + 1, count) # 비숍 배치 없이 다음 인덱스 탐색 경우의 수도 포함

def backtrack_white(el, count):
    global left, right, white_answer

    if el == len(white):
        white_answer = max(white_answer, count)
        return

    r, c = white[el]

    if (left & (1 << r + c)) == 0 and (right & (1 << r - c + (N - 1))) == 0:
        left = left | (1 << r + c)
        right = right | (1 << r - c + (N - 1))
        backtrack_white(el + 1, count + 1)
        left = left & ~(1 << r + c)
        right = right & ~(1 << r - c + (N - 1))

    backtrack_white(el + 1, count) # 비숍 배치 없이 다음 인덱스 탐색 경우의 수도 포함

backtrack_black(0, 0)
backtrack_white(0, 0)
print(black_answer + white_answer)