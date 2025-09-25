N = int(input())

"""
0 <= i < N
0 <= j <= 9
memo[i][j] = 현재 길이가 i일때, 끝자리가 j인 계단수 갯수
"""
memo = [[0 for j in range(10)] for i in range(N)]

for i in range(1, 10):
    memo[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            memo[i][j] = memo[i-1][j+1]
        elif j == 9:
            memo[i][j] = memo[i-1][j-1]
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]

print(sum(memo[N-1]) % 1_000_000_000)