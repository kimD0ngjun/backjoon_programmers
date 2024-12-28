T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)  # dp[k] : k원 만드는 가짓수
    dp[0] = 1  # 0원 만드는 가짓수 : 1개(동전을 아무 것도 주지 않는 가짓수)

    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]

    print(dp[M])