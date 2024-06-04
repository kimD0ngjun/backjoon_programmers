def solution(n, times):
    times.sort()
    answer = 0

    """
    문제 잘 읽을 것. 최적의 값을 찾는 것
    최적화를 해 나가는 과정이므로 이진 탐색이 요구됨
    """
    # 최소로 걸릴 수 있는 시간(가능성)
    left = 1
    # 최대로 걸릴 수 있는 시간(가능성)
    right = max(times) * n

    while left <= right:

        # 현재 탐색된 심사 시간 및 검사 인원
        mid = (left + right) // 2
        human = 0

        for time in times:
            # 심사 시간 당 검사 인원 카운
            human += mid // time

            # 주어진 인원까지만
            if human >= n:
                break

        # 너무 많이 심사함(mid 줄여도 됨)
        # 정답 범위에 현재 mid가 들어가도 됨
        if human >= n:
            answer = mid
            right = mid - 1
        # 너무 부족함(mid를 높여야함)
        else:
            left = mid + 1

    return answer