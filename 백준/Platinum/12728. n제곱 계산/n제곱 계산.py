"""
https://www.acmicpc.net/problem/12728
"""
# 입력
T = int(input())

cases = []

for _ in range(T):
    cases.append(int(input()))

"""
고속 거듭제곱을 썼을 때의 문제점
루트 5와 같은 무리수의 계산에 있어 부동소수점 오차가 필연적으로 발생하기 때문에 완벽한 근사값 계산이 불가능
그래서 예제는 정답이 나오지만 지수가 어어엄청 큰 값들에 대해서는 오차가 발생하는 것 같음
이걸 위해서 일부러 테케를 심각하게 거대한 값으로 넣은 것 같기도 하고....

그럼 고속 거듭제곱을 쓰는 게 아닌가?

---

3 + √5 의 켤레무리수 = 3 - √5

* x, y는 정수

(3 + √5)^N = x + y√5
(3 - √5)^N = x - y√5 = 0.xxx

(3 + √5)^N + (3 - √5)^N = 2x
2x - (3 - √5)^N = 2x - 0.xxx => 정수 부분은 2x - 1

---

고속 거듭제곱 대신 행렬제곱 
-> 정수 제곱은 단위가 2
-> 행렬제곱은 단위를 직접 지정해서 점화식에 포함된 무리수의 제곱꼴 표현 가능

* a, b는 정수

(3 + √5)^N = an + bn√5 이라고 하면
(3 + √5)^N = (3 + √5)(a(n - 1) + b(n - 1)√5)
           = (3a + 5b)(n - 1) + (a + 3b)(n - 1)√5
           
an = (3a + 5b)(n - 1) , bn = (a + 3b)(n - 1)

an   3   5   a(n-1)
   =       *
bn   1   3   b(n-1)

a = 3, b = 1 에서 시작
"""


# 행렬 곱연산(+ 모듈러 연산)
# a, b는 행렬
def matrix(a, b):
    a1, a2, a3, a4 = a
    b1, b2, b3, b4 = b

    r1 = ((a1 * b1) + (a2 * b3)) % 1_000
    r2 = ((a1 * b2) + (a2 * b4)) % 1_000
    r3 = ((a3 * b1) + (a4 * b3)) % 1_000
    r4 = ((a3 * b2) + (a4 * b4)) % 1_000

    return r1, r2, r3, r4


# 고속 거듭제곱 + 행렬 제곱
# N: 지수
def power(N):
    # 단위행렬부터 시작
    result = (1, 0, 0, 1)
    unit = (3, 5, 1, 3)

    while N > 0:
        # 지수가 홀수일 때
        if N % 2 != 0:
            result = matrix(result, unit)

        N = N // 2
        unit = matrix(unit, unit)

    return result


# print(power(1)) # 2제곱
# print(power(2)) # 3제곱

# 출력
for i in range(T):
    r1, r2, r3, r4 = power(cases[i] - 1)

    answer = str(2 * (r1 * 3 + r2) - 1)
    # print(answer)

    if len(answer) > 3:
        answer = answer[-3:]
    elif len(answer) < 3:
        answer = "0" * (3 - len(answer)) + answer

    print(f"Case #{i + 1}: {answer}")
