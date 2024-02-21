import sys
from collections import defaultdict


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

count = int(sys_input())
result = []

for _ in range(count):
    result.append(int(sys_input()))

result.sort()

for i in range(count):
    print(result[i])

