# dp[k][n]: k개의 제곱수로 n을 만드는 방법의 수
dp = [[0] * 32768 for _ in range(5)]
dp[0][0] = 1  # 초기값: 제곱수를 사용하지 않고 0을 만드는 방법은 1가지

max_value = 32768

for i in range(1, int(max_value ** 0.5) + 1):
    square = i * i

    for k in range(1, 5):  # 최대 4개의 제곱수
        for n in range(square, max_value):
            dp[k][n] += dp[k - 1][n - square]

# print(dp)

# input
while True:
    N = int(input())

    if N == 0:
        break

    print(dp[1][N] + dp[2][N] + dp[3][N] + dp[4][N])