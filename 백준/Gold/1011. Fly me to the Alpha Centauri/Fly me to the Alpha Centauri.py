import math
import sys

# 동적계획법으로 풀 수 있을 것 같은데... 생각이 안 난다...

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

results = []

count = int(sys_input())

for _ in range(count):
    start, end = map(int, input().split())
    distance = end - start  # 거리
    ## 제곱이 되는 거리는 계단형으로 오르락 내리락
    # 16은 (루트 16) * 2 - 1
    # 25는 (루트 25) * 2 - 1

    # 해당 거리를 넘지 않는 최대 제곱수(x)부터 해당 거리를 넘는 최소 제곱수(y)까지의 거리 사이의 최대 워프 수
    max_val = int(math.sqrt(distance))

    # 만약 제곱수라면 제곱근 * 2 빼기 1
    if max_val == math.sqrt(distance):
        results.append(max_val * 2 - 1)
    # x의 범위에 포함된 경우
    elif distance <= max_val * max_val + max_val:
        results.append(max_val * 2)
    # y의 범위에 포함된 경우
    else:
        results.append(max_val * 2 + 1)


for result in results:
    print(result)


