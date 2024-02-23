import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

count = int(sys_input())
heap = []

centers = int(sys_input())
censors = list(map(int, sys_input().split()))

# 오름차순 센서 위치 정렬
censors.sort()

# 집중국 배치 : 센서와 센서 간 차이값 위치
# 그 차이값 위치의 크기들 중에서 뽑은 갯수가 곧 집중국 갯수가 된다
position = []

for i in range(len(censors) - 1):
    position.append(censors[i + 1] - censors[i])

position.sort()

# 집중국은 늘 센서 개수 + 1개의 범위를 커버할 수 있다.
# 예를 들어서 센서가 2개 있으면 집중국은 최소 1개로, 2개의 센서를 커버 가능
# 센서가 3개일 경우, 1개의 집중국이 3개 전부를 + 최소 2개의 집중국이 차이값 각각 맡으며 커버 가능
# 집중국의 개수가 주어질 때, 센서 - 1개의 집중국이 센서 차이값(위치)들을 최대의 효율이긴 하지만
# 문제에서는 그게 안 되므로 차이값들 2개 이상씩 커버하는 경우가 나오게 되는데,
# 최대한 작은 차이값을 커버시켜야 절약이 가능
# 그래서 position을 오름차순하고 censor + 1까지의 인덱스까지의 합 도출
# 즉 최대한 먼 센서간 거리는 비우고 최대한 가까이 몰려있는 센서들끼리 집중국이 커버하는 것이 이

# 인덱스가 len(position) - centers + 1인 이유는
# 위에서 봤듯이 centers - 1개의 거리값을 선택해야 되고
# 참조시킬 범위를 전체 포지션 길이에서 centers - 1을 뺀 값으로 최대 인덱스 범위를 지정하는 셈
print(sum(position[:len(position) - centers + 1]))

