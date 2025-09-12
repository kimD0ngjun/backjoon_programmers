# https://www.acmicpc.net/problem/11003
import sys

input = sys.stdin.readline

# 입력
n = int(input())

MOD = 1_000_000_007

def matrix(a, b):
    a1, a2, a3, a4 = a
    b1, b2, b3, b4 = b

    r1 = ((a1 * b1) + (a2 * b3)) % MOD
    r2 = ((a1 * b2) + (a2 * b4)) % MOD
    r3 = ((a3 * b1) + (a4 * b3)) % MOD
    r4 = ((a3 * b2) + (a4 * b4)) % MOD

    return r1, r2, r3, r4

def power(N):
    result = (1, 0, 0, 1)
    unit = (1, 1, 1, 0)

    while N > 0:
        if N % 2 != 0:
            result = matrix(result, unit)

        N = N // 2
        unit = matrix(unit, unit)

    r1, r2, _, _ = result

    return r1 + r2

print(power(n - 2) % MOD)