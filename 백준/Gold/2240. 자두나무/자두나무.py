T, W = map(int, input().split())  # t: 시점, w: 최대 이동 횟수
memo = [[0] * (W + 1) for _ in range(T + 1)]

# 자두 순서대로 탐색(i: 자두의 순서)
for i in range(1, T + 1):
    plum = int(input())  # 자두가 1인지 2인지 받기

    # j번 이동했을 때 각 케이스 카운팅
    for j in range(W + 1):
        if j == 0:
            # 첫 번째 이동에서만 +1 (그냥 나무에 떨어지는 경우)
            if plum == 1:
                memo[i][j] = memo[i - 1][j] + 1
            else:
                memo[i][j] = memo[i - 1][j]
            continue

        if j % 2 == 0:  # 짝수번 이동(제자리 1번 복귀)
            if plum == 1:  # 이 과정에서 1번에서 자두가 떨어지면
                memo[i][j] = max(memo[i - 1][j] + 1, memo[i - 1][j - 1])  # 같은 나무에 떨어지면 +1, 다른 나무로 이동하면 +0
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1] + 1)  # 얘도 마찬가지
        else:  # 홀수번 이동(결국 2번 나무에 위치한 셈)
            if plum == 1:  # 이 과정에서 1번에서 자두가 떨어지면
                memo[i][j] = max(memo[i - 1][j - 1] + 1, memo[i - 1][j])
            else:
                memo[i][j] = max(memo[i - 1][j - 1], memo[i - 1][j] + 1)

# 최대값 찾기
answer = 0

for k in range(W + 1):
    answer = max(answer, memo[T][k])

print(answer)