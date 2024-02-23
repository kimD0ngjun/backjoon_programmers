import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

count = int(sys_input())
provinces = list(map(int, sys_input().split()))
all_budgets = int(sys_input())

provinces.sort()
result = 0

# 재귀 커스터마이징 재도전
def binary_search(provinces, all_budgets, minimum, maximum):
    if minimum > maximum:
        return maximum

    limit = (maximum + minimum) // 2  # 상한액 계산
    total_sum = 0

    # 상한액 이하의 예산을 모두 합산
    for budget in provinces:
        total_sum += min(limit, budget)

    # 상한액을 넘지 않으면 최대 상한액을 업데이트
    # 더 큰 상한액을 찾기 위해 범위를 늘림
    if total_sum <= all_budgets:
        return binary_search(provinces, all_budgets, limit + 1, maximum)  # 다음 탐색에서 중복된 중간값을 제외하기 위해 더하기 1
    # 그렇지 않으면 상한액 초과니까 최대 금액을 줄여서 다시 상한액 계산
    else:
        return binary_search(provinces, all_budgets, minimum, limit - 1)  # 다음 탐색에서 중복된 중간값을 제외하기 위해 빼기 1


# 이진 탐색 커스터마이징
## 흠... 왜 재귀로는 안 될까
minimum, maximum = 0, max(provinces)

# while minimum <= maximum:
#     limit = (maximum + minimum) // 2 # 상한액 계산
#     total_sum = 0
#
#     # 상한액 이하의 예산을 모두 합산
#     for budget in provinces:
#         total_sum += min(limit, budget)
#
#     # 상한액을 넘지 않으면 최대 상한액을 업데이트
#     # 더 큰 상한액을 찾기 위해 범위를 늘림
#     if total_sum <= all_budgets:
#         result = limit
#         minimum = limit + 1 # 다음 탐색에서 중복된 중간값을 제외하기 위한 더하기 1
#     # 그렇지 않으면 상한액 초과니까 최대 금액을 줄여서 다시 상한액 계산
#     else:
#         maximum = limit - 1 # 다음 탐색에서 중복된 중간값을 제외하기 위한 빼기 1

print(binary_search(provinces, all_budgets, 0, max(provinces)))
