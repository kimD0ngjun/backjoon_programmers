import sys

if __name__ == "__main__":
    coins = []
    n, k = map(int, input().split())

    for _ in range(n):
        coins.append(int(input()))

    memo = [sys.maxsize] * (k + 1)  # 인덱스에 해당하는 금액을 만들기 위한 최소 동전 개수
    memo[0] = 0  # 0원 경우의 수는 0개

    for coin in coins:
        for i in range(coin, k + 1):
            """
            여기서 + 1에서의 1은, 현재 coin 분기 바로 직전의 coin을 의미
            예를 들어 현재 coin이 5라면 저 + 1 은 바로 이전 코인인 1을 더한 개수가 됨
            """
            memo[i] = min(memo[i], memo[i - coin] + 1)

    if memo[k] == sys.maxsize or 0:
        print(-1)
    else:
        print(memo[k])