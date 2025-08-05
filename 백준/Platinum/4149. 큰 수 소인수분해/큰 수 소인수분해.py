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

# 인수 연산기
def pollard_rho(n):
    if n % 2 == 0:
        return 2

    # c의 변동을 통한 확률적 실패 대응
    for c in range(1, 10):
        xi = 2
        xj = 2
        d = 1
        f = lambda x: (x * x + c) % n

        while d == 1:
            xi = f(xi)
            xj = f(f(xj))

            d = math.gcd(abs(xi - xj), n)

        if d != n and d != 1:
            return d

    return None

# 입력기
def sys_input():
    return sys.stdin.readline().strip()

# 풀이 시작
n = int(sys_input())

# 밀러 라빈 알고리즘 준비
mr = miller_rabin()

# 소인수 구하는 메소드
factors = []

def prime_factors(x):
    # 더이상 분해할 게 x
    if x == 1:
        return

    # 소인수 탐색 성공
    if mr.cal(x):
        factors.append(x)
        return

    # 여전히 합성수라면 폴라드 로 재귀 적용
    d = pollard_rho(x)

    if d is None or d == x:
        factors.append(x)
        return

    prime_factors(d)
    prime_factors(x//d)

if n == 1:
    print(1)
elif mr.cal(n):
    print(1)
    print(n)
else:
    prime_factors(n)
    print(*factors, sep='\n')