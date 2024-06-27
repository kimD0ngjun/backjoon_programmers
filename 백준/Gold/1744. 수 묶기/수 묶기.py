"""
https://www.acmicpc.net/problem/1744
"""
from collections import deque

# 입력 처리
N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))

"""
N의 케이스가 50까지밖에 안되니까 sort()로도 충분히 정렬이 가능할듯

plus랑 minus랑 zero랑 나눠서 생각
"""

answer = 0

natural = []
negative = []
zero = False

for num in nums:
    if num > 0:
        natural.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero = True

# 자연수는 내림차순 정렬
natural.sort(reverse=True)
negative.sort()

# 자연수는 내림차순 정렬
natural.sort(reverse=True)
# 음수는 오름차순 정렬
negative.sort()

# 짝짓기하여 곱셈
for i in range(0, len(natural) - 1, 2):
    # 두 개의 자연수 묶기, 단 1은 더하는 것이 이득이므로 따로 처리
    if natural[i + 1] != 1:
        answer += natural[i] * natural[i + 1]
    else:
        answer += natural[i] + natural[i + 1]

# 남아 있는 자연수가 있을 경우 더하기
if len(natural) % 2 == 1:
    answer += natural[-1]

# 음수를 짝짓기하여 곱셈
for i in range(0, len(negative) - 1, 2):
    answer += negative[i] * negative[i + 1]

# 남아 있는 음수가 있을 경우 0이 있으면 음수를 없애고,
# 그렇지 않으면 그 음수를 더함
if len(negative) % 2 == 1:
    if not zero:
        answer += negative[-1]

# 결과 출력
print(answer)