import sys

def solution(distance, rocks, n):
    answer = 0

    # distance -> 수직선 위의 점 0에서 점 distance(양수)까지의 거리
    # rocks에서 n개만큼 요소를 뺀다
    # 이진 탐색의 전제 조건은 '정렬된' 리스트
    rocks.sort()
    rocks = [0] + rocks + [distance]

    # print("rocks: " + str(rocks))

    intervals = []

    for i in range(1, len(rocks)):
        intervals.append(rocks[i] - rocks[i - 1])

    # print("intervals: " + str(intervals))

    # 간격을 이분 탐색하기
    # 최소 간격(1)과 최대 간격(distance) 각각 왼쪽 오른쪽으로 배치
    left = 1
    right = distance

    # 중간 인덱스 초기화
    mid = (left + right) // 2

    # 역전이 되기 전까지
    while left <= right:

        # 돌 삭제 카운트
        remove_count = 0
        # mid를 넘지 않는 이어진 간격들 산정값
        current = 0

        for interval in intervals:
            current += interval

            # 여전히 현재 간격들 합이 mid보다 작을 때마다
            # 현재 임의 설정된 최대값인 mid에 가까워지기 위해
            # remove_count를 늘여도 좋다
            if current < mid:
                remove_count += 1
            # 만약 아니라면 다시 초기화해준다
            else:
                current = 0

        # remove 카운트보다 요구 삭제값(n)이 작으면
        # mid 값 너무 크니까 줄여야 됨
        if remove_count > n:
            right = mid - 1
        # 그 반대면 mid 값 적당하니까 더 제거해도 괜찮음
        else:
            left = mid + 1

        # 중간 인덱스 업뎃
        mid = (left + right) // 2

    return mid

# print(solution(25, [2, 14, 11, 21, 17], 2))