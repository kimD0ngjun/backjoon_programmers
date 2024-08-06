"""
https://www.acmicpc.net/problem/1461
"""
import sys


# 입력
def sys_input():
    return sys.stdin.readline().rstrip()


_, M = map(int, input().split())
books = list(map(int, sys_input().split()))

"""
1. 가장 멀리 있는 책 위치는 가장 마지막 걸음이 되어야 한다
2. 1번의 과정에서 최대 M개의(먼 책까지 포함해서) 먼 책들을 갖다 놓는다.
3. 역순으로 수행했을 때, N % M 개의 남은 가장 가까운 애들이 처리된다
4. 음수 위치의 책과 양수 위치의 책은 서로 별개의 계산으로 수행한다(단 2번 제외)
"""

# 연산
positive = []
negative = []

for book in books:
    if book > 0:
        positive.append(book)
    else:
        negative.append(book)

positive.sort(reverse=True)
negative.sort()

# print(positive)
# print(negative)

# 가장 마지막에 가져다 놓을 위치 산정
# 딱 한 번만 걷게 할 위치
# 양의 위치와 음의 위치가 같아도 상관 x
last = 0

if positive and not negative:
    last = positive[0]
elif negative and not positive:
    last = negative[0]
else:
    if positive[0] > -negative[0]:
        last = positive[0]
    else:
        last = negative[0]

# print(last)

walk = 0
is_calculated = False  # 동일 먼 거리일 때의 중복 계산 방지

# positive 연산
for i in range(0, len(positive), M):
    # 가장 먼 책일 경우
    if positive[i] == last:
        walk += positive[i]
        is_calculated = True
        continue

    walk += 2 * positive[i]

# negative 연산
for i in range(0, len(negative), M):
    # 가장 먼 책일 경우
    if negative[i] == last and not is_calculated:
        walk -= negative[i]
        continue

    walk -= 2 * negative[i]

print(walk)
