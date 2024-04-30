# i == 줄, j == 요소
def recursion(triangle, i, j, memo):
    # 탈출 조건
    if i == len(triangle) - 1:
        return triangle[i][j]

    # memoization
    if memo[i][j] != -1:
        return memo[i][j]

    # 왼쪽 아래
    left = recursion(triangle, i + 1, j, memo)
    # 오른족 아래
    right = recursion(triangle, i + 1, j + 1, memo)

    # 재귀함수 특징 활용
    memo[i][j] = triangle[i][j] + max(left, right)

    return memo[i][j]


# 입력 단계 및 memoization 준비
count = int(input())
memo = []
triangle = []

for i in range(count):
    memo.append([-1] * (i + 1))
    triangle.append(list(map(int, input().split())))

print(recursion(triangle, 0, 0, memo))