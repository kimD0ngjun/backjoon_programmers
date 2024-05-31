import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline()

class MillerRabin:
    """
    거듭제곱을 그냥 계산하면 시간 복잡도가 O(N)이므로
    고속 거듭제곱 알고리즘 차용
    """

    # a는 밑 b는 지수, N은 모듈러 연산 대상이자 소수 판별 대상
    def power(self, a, b, N):

        result = 1

        while b > 0:
            # b가 홀수일 경우
            if b % 2 != 0:
                # result에 밑 한 번 더 곱하고
                # 오버플로우 발생 방지용 모듈러 연산(% m)
                result = (result * a) % N

            # 제곱한 만큼 b는 2로 나눠주고
            # 홀수, 짝수 상관없이 a는 제곱
            # 오버플로우 발생 방지용 모듈러 연산(% m)
            b = b // 2
            a = (a * a) % N

        return result

    # N은 소수 판별 대상, t는 소수성 테스트용 기반 숫자
    def test(self, N, t):

        # 거듭제곱 지수 초기화
        r = 0
        # 짝수 초기화
        n = N - 1

        # 거듭제곱 지수 카운팅
        while n % 2 == 0:
            r += 1
            n = n // 2

        # t^(N-1) 즉, t^n 계산
        x = self.power(t, n, N)

        # x == 1 : t^n ≡ 1 (mod N) 판별
        # x == N - 1 : t^n ≡ -1 (mod N) 판별
        if x == 1 or x == N - 1:
            return True

        # t^(2^(r-1) * n) ≡ -1 (mod N) 판별
        for i in range(0, r - 1):
            # x = x^2 mod N 갱신 계산
            x = self.power(x, 2, N)

            # 여기서 판별
            if x == N - 1:
                return True

        # 저 두 조건 다 만족 못하면 그냥 합성수
        return False


cases = int(sys_input())
mr = MillerRabin()
count = 0

for _ in range(cases):

    N = int(sys_input())

    """
    2xy + x + y = N
    2x(y + 1/2) + y + 1/2 = N + 1/2
    (2x + 1)(y + 1/2) = N + 1/2
    (2x + 1)(2y + 1) = 2N + 1       --- > 두 홀수의 곱으로 이뤄짐 == 소수가 아님

    2N + 1을 했을 때 소수가 나오면 카운팅
    """

    temp = True
    N = 2 * N + 1

    # if mr.test(N, 2):
    #     count += 1

    for i in [2, 3, 5, 11]:
        if mr.test(N, i):
            continue
        else:
            temp = False
            break

    if temp:
        count += 1

print(count)