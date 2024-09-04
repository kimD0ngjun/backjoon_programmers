"""
https://www.acmicpc.net/problem/2023
"""


# 밀러 라빈 클래스 정의
class MillerRabin:
    """
    # a는 밑 b는 지수, N은 모듈러 연산 대상이자 소수 판별 대상
    """
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


# 입력
N = int(input())

# 얀신
base_prime = [2, 3, 5, 7]

mr = MillerRabin()

while len(str(base_prime[0])) < N:

    temp = []

    for prime in base_prime:
        for i in range(1, 10):

            str_prime = str(prime) + str(i)

            # 이전 판별 소수와 현재 판별 소수 간의 밀러 라빈 테스트
            if mr.test(int(str_prime), prime):
                temp.append(int(str_prime))

    base_prime = temp

# 출력
for prime in base_prime:
    print(prime)