"""
https://www.acmicpc.net/problem/27435
"""
# 입력
T = int(input())

MOD = 998_244_353

"""
- 점화식
P(N) = P(N-1) + P(N-5)
P(N) = P(N-2) + P(N-3)

P(N-1) = P(N-3) + P(N-4)
P(N-1) = P(N-2) + P(N-5)

P(N-2) = P(N-4) + P(N-5)
P(N-2) = P(N-3) + P(N-6)

P(N+1) = P(N-1) + P(N-2)

- 행렬 점화식
0 1 1   P(N)   P(N+1)
1 0 0 * P(N-1) = P(N)
0 1 0   P(N-2)   P(N+1)
"""


# 행렬 연산 메소드(3 x 3)
def matrix(a, b):
    a1, a2, a3, a4, a5, a6, a7, a8, a9 = a
    b1, b2, b3, b4, b5, b6, b7, b8, b9 = b

    r1 = (a1 * b1 + a2 * b4 + a3 * b7) % MOD
    r2 = (a1 * b2 + a2 * b5 + a3 * b8) % MOD
    r3 = (a1 * b3 + a2 * b6 + a3 * b9) % MOD

    r4 = (a4 * b1 + a5 * b4 + a6 * b7) % MOD
    r5 = (a4 * b2 + a5 * b5 + a6 * b8) % MOD
    r6 = (a4 * b3 + a5 * b6 + a6 * b9) % MOD

    r7 = (a7 * b1 + a8 * b4 + a9 * b7) % MOD
    r8 = (a7 * b2 + a8 * b5 + a9 * b8) % MOD
    r9 = (a7 * b3 + a8 * b6 + a9 * b9) % MOD

    return r1, r2, r3, r4, r5, r6, r7, r8, r9


# 고속 거듭제곱 + 행렬 제곱
# N: 지수
def power(N):
    # 단위행렬부터 시작
    result = (1, 0, 0, 0, 1, 0, 0, 0, 1)
    unit = (0, 1, 1, 1, 0, 0, 0, 1, 0)

    while N > 0:
        # 지수가 홀수일 때
        if N % 2 != 0:
            result = matrix(result, unit)

        N = N // 2
        unit = matrix(unit, unit)

    return result


# print(power(0)) # 1제곱(그냥 그대로)
# print(power(1)) # 2제곱

# 연산

answers = []

for _ in range(T):
    case = int(input())

    if case == 1 or case == 2 or case == 3:
        answers.append(1)
        continue

    r1, r2, r3, r4, r5, r6, r7, r8, r9 = power(case - 3)
    answers.append((r1 + r2 + r3) % MOD)

for answer in answers:
    print(answer)