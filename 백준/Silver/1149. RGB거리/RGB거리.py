import sys


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# DP 함수
def min_cost_to_paint(count, costs):
    # 이전 집에 특정 색을 칠하면 다음 집은 두 가지 경우의 수(그 중 최소값)
    # 집을 색칠하며 더해가는 식으로 카운팅
    # 특정 분기의 집의 색을 고를 때, 반대로 생각하기?
    # 이전 집의 최소 비용은 얼마가 들었나?
    # 약간 집 털기 문제 느낌이 나는데?

    choose = [[0, 0, 0] for _ in range(count)] # 선택 마련
    choose[0] = costs[0] # 선택 마련을 위한 초기화

    for i in range(1, count):
        # 각각의 집 선택에 있어 이전 집에서의 어떤 최소값을 산출하게 되는지를 경우의 수를 따지기
        # 앞선 값들의 최소합들이 이전 인덱스에 담겨있을 것
        choose[i][0] = min(choose[i-1][1], choose[i-1][2]) + costs[i][0]
        choose[i][1] = min(choose[i-1][0], choose[i-1][2]) + costs[i][1]
        choose[i][2] = min(choose[i-1][0], choose[i-1][1]) + costs[i][2]

    # 그럼 맨 마지막 집 선택한 것 중 가장 저렴한 비용이 곧 최대한 절약한 최소값
    return min(choose[count - 1])


count = int(sys_input())
costs = []

for i in range(count):
    cost = list(map(int, sys_input().split()))
    costs.append(cost)

print(min_cost_to_paint(count, costs))