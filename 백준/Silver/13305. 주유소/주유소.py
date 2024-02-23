import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 첫 번째 도시에는 무조건 기름을 넣어야 한다
# 모든 길에서 드는 기름
# 가장 가격 덜 잡아먹는 도시에서 최대한 많이 채우고
# 그 다음 채우고... 등등

count = int(sys_input())

amounts = [int(amount) for amount in sys_input().split()] # 도로당 기름 소모양
costs = [int(cost) for cost in sys_input().split()] # 도시별 리터당 비용

# 첫 도시에서는 언제나 기름이 비어있으므로
# 첫 도로를 건너기 위한 최소한의 기름을 무조건 채워야만 한다
minimum_cost = costs[0]
all_cost = amounts[0] * minimum_cost

# 마지막 도시에 도달했을 때 0리터인 게 최상의 시나리오이므로
# 범위는 마지막 도시 직전까지(count - 1)
for i in range(1, count - 1):
    # 이후의 도시 기름값이 현재 위치의 도시 기름값보다 높으면
    # 굳이 거기서 채울 필요가 없음
    if minimum_cost <= costs[i]:
        all_cost += minimum_cost * amounts[i] # 다음 도시 몫까지 현재 도시에서 채우기
    # 만약 차후 도시 기름값이 더 싸다면
    # 다음 도시에서 다음 도로부터의 기름을 채우고 최소 기름값을 업데이트함
    else:
        all_cost += costs[i] * amounts[i]
        minimum_cost = costs[i]

print(all_cost)