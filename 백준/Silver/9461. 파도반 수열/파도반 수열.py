memo = {}

def recursion(n):
    if 1 <= n <= 3:
        memo[n] = 1
        return 1

    if 4 <= n <= 5:
        memo[n] = 2
        return 2

    # memoization
    if n in memo:
        return memo[n]

    memo[n] = recursion(n - 1) + recursion(n - 5)
    return memo[n]


# 입력 단계
count = int(input())

for _ in range(count):
    print(recursion(int(input())))