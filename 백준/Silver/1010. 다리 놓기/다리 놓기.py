# 조합 계산을 위한 팩토리얼 함수
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 정답 리스트 세팅
results = []


# 입력 단계
case = int(input())

for _ in range(case):
    M, N = map(int, input().split())

    if M >= N:
        n = M
        r = N
    else:
        n = N
        r = M

    # nCr
    result = factorial(n) // (factorial(r) * factorial(n - r))
    results.append(result)


# Answer
for result in results:
    print(result)

