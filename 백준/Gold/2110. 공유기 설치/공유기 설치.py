"""
https://www.acmicpc.net/problem/2110
"""
import sys
input = sys.stdin.readline

houses = []
cases, router_counts = map(int, input().split())

for _ in range(cases):
    houses.append(int(input()))

houses.sort()

# print(houses)

# 이진탐색 시작
left = 1
right = houses[len(houses)-1] - houses[0]

result = 0

while left <= right:
    # 중간 인덱스 업뎃
    # 최소 거리를 mid로 가정
    mid = (left + right) // 2

    # 어차피 처음 시작점에서 무조건 라우터 설치할 테니(최소 거리 중 최대값)
    setting_count = 1
    # 탐색할 때 마지막 집(거리 산출을 위한 값)
    last = houses[0]

    for i in range(1, len(houses)):
        # 만약 마지막 탐색집과 현재 집 간의 거리가 mid 이상이면
        # 범위를 넘어선거니까 공유기 설치가 필요해짐
        if houses[i] - last >= mid:
            setting_count += 1

            # last 업데이트
            last = houses[i]

            # 제공된 공유기 수에 다다라 넘어서면 반복문 파괴
            if router_counts <= setting_count:
                break

    # 여전히 아리송한 부분....
    if router_counts <= setting_count:
        result = mid
        left = mid + 1
    else:
        right = mid - 1


print(result)
