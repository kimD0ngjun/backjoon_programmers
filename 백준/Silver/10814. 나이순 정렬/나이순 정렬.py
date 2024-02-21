import sys
from collections import defaultdict

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

count = int(sys_input())
input = []

for _ in range(count):
    input.append([int(x) if x.isdigit() else x for x in sys_input().split()])

result = sorted(input, key=lambda x: x[0])

for item in result:
    result_str = ' '.join(map(str, item))
    print(result_str)