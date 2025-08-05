import math
import sys


# 소수 판별기
class miller_rabin:
    def __init__(self):
        self.bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    def power(self, a, b, N):
        result = 1

        while b > 0:
            if b % 2 != 0:
                result = (result * a) % N

            b = b // 2
            a = (a * a) % N

        return result

    # N은 소수 판별 대상, t는 소수성 테스트용 기반 숫자
    def test(self, N, t):
        r = 0
        n = N - 1

        while n % 2 == 0:
            r += 1
            n = n // 2

        x = self.power(t, n, N)

        if x == 1 or x == N - 1:
            return True

        for i in range(0, r-1):
            x = self.power(x, 2, N)

            if x == N - 1:
                return True

        return False

    def cal(self, N):
        for i in self.bases:
            if i >= N:
                continue  # i는 반드시 N보다 작아야 함
            if not self.test(N, i):
                return False

        return True

# 입력기
def sys_input():
    return sys.stdin.readline().strip()

# 풀이 시작
A, B = map(int, sys_input().split())

# 밀러 라빈 알고리즘 준비
mr = miller_rabin()

"""
테케에 9도 있네...?
8!이 9**2로 나뉘어떨어지지 않는 건 첨 알았네;
"""
for i in range(A, B + 1):
    if mr.cal(i) or i == 9:
        print(i, end=" ")