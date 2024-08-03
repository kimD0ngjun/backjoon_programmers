"""
https://www.acmicpc.net/problem/2749
"""
# 입력
n = int(input())

MOD = 1_000_000

"""
- 행렬 점화식
1 1     P(N)    P(N+1)
      *       =
1 0    P(N-1)    P(N)
"""


# 행렬 연산 메소드(2 x 2)
# 행렬 곱연산(+ 모듈러 연산)
# a, b는 행렬
def matrix(a, b):
    a1, a2, a3, a4 = a
    b1, b2, b3, b4 = b

    r1 = ((a1 * b1) + (a2 * b3)) % MOD
    r2 = ((a1 * b2) + (a2 * b4)) % MOD
    r3 = ((a3 * b1) + (a4 * b3)) % MOD
    r4 = ((a3 * b2) + (a4 * b4)) % MOD

    return r1, r2, r3, r4


# 고속 거듭제곱 + 행렬 제곱
# N: 지수
def power(N):
    # 단위행렬부터 시작
    result = (1, 0, 0, 1)
    unit = (1, 1, 1, 0)

    while N > 0:
        # 지수가 홀수일 때
        if N % 2 != 0:
            result = matrix(result, unit)

        N = N // 2
        unit = matrix(unit, unit)

    r1, r2, _, _ = result

    return r1 + r2


# print(power(1))
# print(power(3))
# print(power(5))
# print(power(998))

# 연산
print(power(n - 2) % MOD)
