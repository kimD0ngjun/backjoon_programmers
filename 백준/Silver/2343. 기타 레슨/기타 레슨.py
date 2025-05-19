# 알고리즘 감각 다시 살리기...
# 블루레이가 다른 게 아니라 수열 부분합이었음
# 백준 설명 드럽게 못하네 진심
N, M = map(int, input().split())
courses = list(map(int, input().split()))

right = sum(courses)
left = max(courses)

while left <= right:
    # print("반복반복")
    mid = (left + right) // 2
    sum_value = 0
    count = 0 # 블루레이 개수

    for course in courses:
        if sum_value + course > mid:
            sum_value = course
            count += 1
        else:
            sum_value += course

    if sum_value != 0:
        count += 1

    # 합산 다 끝내고 카운트 비교
    if count <= M: # M개 혹은 더 작은 갯수로도 충분히 가능?
        right = mid - 1 # right를 더 좁혀서 더 작은(극단적인) 용량으로 시도
    else: # M개를 넘겨서 정답이 안된다면
        left = mid + 1 # 용량을 키워야 함(널널하게)

# 블루레이 크기 중 최소를 구해야 하므로
print(left)
