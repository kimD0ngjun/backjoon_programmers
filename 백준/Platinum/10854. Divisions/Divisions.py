import math
import sys
from collections import defaultdict

input = sys.stdin.readline

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

def pollard_rho(n):
    if n % 2 == 0:
        return 2

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

def factorize(n):
    factors = defaultdict(int)
    mr = miller_rabin()

    def factor(n):
        if n == 1:
            return
        
        if mr.cal(n):
            factors[n] += 1
            return
        
        d = pollard_rho(n)
        
        if d is None:
            factors[n] += 1
            return
        
        factor(d)
        factor(n // d)

    factor(n)
    return factors

N = int(input())
factors = factorize(N)

result = 1
for exp in factors.values():
    result *= (exp + 1)

print(result)