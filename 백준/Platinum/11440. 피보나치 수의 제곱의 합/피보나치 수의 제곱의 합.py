# 머리 좀 말랑말랑하게 하기...
MOD = 1_000_000_007


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

    # N번째 피보나치 행렬 반환
    return result


# 피보나치 제곱 합
# 공식 : S(N) = Fn * F(n+1)
def fibonacci_square(N):
    if N == 0:
        return 0

    F, _, _, _ = power(N - 1)
    next_F, _, _, _ = power(N)

    return (F * next_F) % MOD


n = int(input())
print(fibonacci_square(n))