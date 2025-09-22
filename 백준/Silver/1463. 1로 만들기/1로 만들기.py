import sys

N = int(input())
# answer = sys.maxsize
#
# def recur(n, count):
#     global answer
#
#     if n == 1:
#         answer = min(answer, count)
#         return
#
#     if n % 2 == 0:
#         recur(n / 2, count + 1)
#     if n % 3 == 0:
#         recur(n / 3, count + 1)
#
#     recur(n - 1, count + 1)
#
# recur(N, 0)
# print(answer)

"""
당연히 이러면 시간초과 날 테고...
memo[n] = n을 1로 만드는 최소 연산 횟수

memo[n] = memo[n - 1] + 1

if n % 2 == 0:
    memo[n] = min(memo[n // 2] + 1, memo[n])
if n % 3 == 0:
    memo[n] = min(memo[n // 3] + 1, memo[n])
"""

if N == 1:
    print(0)
elif N == 2:
    print(1)
elif N == 3:
    print(1)
else:
    memo = [0 for _ in range(N + 1)]
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1

    for i in range(4, N + 1):
        memo[i] = memo[i - 1] + 1

        if i % 2 == 0:
            memo[i] = min(memo[i // 2] + 1, memo[i])
        if i % 3 == 0:
            memo[i] = min(memo[i // 3] + 1, memo[i])

    print(memo[N])