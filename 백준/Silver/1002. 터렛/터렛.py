import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 두 원의 교점 구하기
results = []
count = int(sys_input())

for _ in range(count):
    x1, y1, r1, x2, y2, r2 = map(int, sys_input().split())
    # 두 원의 중심 간의 거리의 제곱을 계산
    squared_diff = (x2 - x1) ** 2 + (y2 - y1) ** 2

    # 두 원의 반지름의 합과 차 계산
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)

    # 두 점 간 거리 기준 내외접 분별
    if squared_diff == 0:
        # 두 원의 중심이 같을 때
        if r1 == r2:
            results.append(-1)  # 원이 겹침
        else:
            results.append(0)  # 원이 겹치지 않음
    else:
        if squared_diff == r_sum**2 or squared_diff == r_diff**2:
            results.append(1)  # 외접 or 내접
        elif r_diff**2 < squared_diff < r_sum**2:
            results.append(2)  # 두 점에서 만남
        else:
            results.append(0)  # 만나지 않음

for result in results:
    print(result)
