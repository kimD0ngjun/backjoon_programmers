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

    return None;

# 입력기
def sys_input():
    return sys.stdin.readline().strip()

# 풀이 시작
n = int(sys_input())

"""
1. n이 소수인가? 그럼 정답은 n-1 바로 프로그램 종료
2. 아니다. 그럼 소인수분해가 가능하므로 폴라드 로 적용
3. 2번에서 재귀 적용을 통해 소인수를 구한다
4. 여기서 오일러 피 함수 적용(https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%ED%94%BC_%ED%95%A8%EC%88%98)
n이 소수가 아니라면 소인수를 구해서 
각각 n * (1-(1/소인수 P)) * (1-(1/소인수 Q)) ...
"""

# 밀러 라빈 알고리즘 준비
mr = miller_rabin()

# 소인수 구하는 메소드
factors = set()

def prime_factors(x):
    # 더이상 분해할 게 x
    if x == 1:
        return

    # 소인수 탐색 성공
    if mr.cal(x):
        factors.add(x)
        return

    # 여전히 합성수라면 폴라드 로 재귀 적용
    d = pollard_rho(x)

    if d is None or d == x:
        factors.add(x)
        return

    prime_factors(d)
    prime_factors(x//d)

if n == 1:
    print(1)
elif mr.cal(n):
    print(n - 1) # 1번
else:
    prime_factors(n)
    answer = n

    for el in factors:
        answer = answer // el * (el - 1)

    print(answer)

