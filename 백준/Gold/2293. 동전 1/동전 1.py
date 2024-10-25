if __name__ == "__main__":
    coins = []
    n, k = map(int, input().split())

    for _ in range(n):
        coins.append(int(input()))

    memo = [0] * (k + 1)
    memo[0] = 1  # 0원 경우의 수는 1개

    for coin in coins:
        for i in range(coin, k + 1):
            """
            * memo[i] : i원을 만들기 위한 경우의 수(반복문 분기마다 누적됨)
            ex) 7원을 만들기 위한 경우의 수 : memo[7]
            
            만약 7원(i)을 만들기 위해 2원(coin)을 추가한다면 
            그 전의 경우의 수인 5원(i - coin) 만드는 경우의 수를 더한다
            (더하기 전의 memo[7]의 값은 2원을 만드는 경우의 수까지 계산된 시점)
            
            * 경우의 수 계산에서의 합의 법칙
            """
            memo[i] += memo[i - coin]

    print(memo[k])