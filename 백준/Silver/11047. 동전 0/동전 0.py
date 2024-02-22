import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 계산 함수
def calculate(kinds, value):
    if value == 0 or not kinds:
        return 0

    count = 0
    max_index = len(kinds) - 1

    while max_index >= 0:
        max_value = kinds[max_index] # 최대 동전
        count += value // max_value # 해당 동전 카운팅
        value %= max_value # 최대 동전 값어치 할당 후 나머지
        max_index -= 1 # 최대 동전 다운

    return count

# 입력 처리
cases, value = map(int, sys_input().split())
kinds = []

for _ in range(cases):
    kinds.append(int(sys_input()))

print(calculate(kinds, value))
