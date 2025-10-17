N, M = map(int, input().split())

"""
1. 통장에서 K원을 인출한다
1-1. 하루를 보내면 그대로 소진한다
1-2. 하루를 못 보내면 그제야 K원을 다시 인출한다

N개의 나열된 일별 사용금액을, M개의 구간으로 나눠야 되는데
M개의 구간으로 나누는 각각의 경우의 수마다 해당 단위구간들 중 사용 금액이 가장 큰 것들을 map
그리고 그 map한 리스트에서 가장 최소값을 뽑음
"""
"""
이진탐색 문제 유형
1. 배열 이진탐색
2. 범위 이진탐색 -> 파라메트릭 서치 유형 연습 좀 더 해야될듯
"""
costs = [int(input()) for _ in range(N)]

# 예상한 인출금액 내에서 M번 커버가 가능한가?
def check(w):
    idx = 1 # 첫날부터 돈이 필요할 테니
    use = 0

    for cost in costs:
        # exception: 인출 금액보다 더 큰 cost면 걍 불가능
        if cost > w:
            return False

        # 사용합산액이 인출액을 넘어서면 인출 횟수 +1 & 사용금액 초기화
        if use + cost > w:
            idx += 1
            use = 0

        use += cost

        # 인출 횟수가 문제의 제시 인출 횟수를 넘어서면 불가능
        if idx > M:
            return False

    # 도달했으면 가능
    return True

# 최소 인출액(비용들 중 최대액) 하한과 최대 인출액(비용 총합) 상한
min_withdraw = max(costs)
max_withdraw = sum(costs)
answer = max_withdraw

while min_withdraw <= max_withdraw:
    mid = (max_withdraw + min_withdraw) // 2

    # mid 금액 범위에서 인출 가능하다면
    if check(mid):
        # 상한선 더 줄여보기
        max_withdraw = mid - 1
        answer = mid
    # 불가능하다면
    else:
        min_withdraw = mid + 1

print(answer)
