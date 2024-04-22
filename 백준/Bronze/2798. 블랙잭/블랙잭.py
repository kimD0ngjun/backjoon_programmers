# 조합 함수(dfs 기반)
def combine(cards: list): # cards: 카드 리스트
    result = []

    # cur: 현재 인덱스, visit: 방문한 숫자 리스트
    def dfs(cur, visit):
        # 백트랙킹
        if len(visit) == 3:
            # visit에 영향 안 가게 복사 객체
            result.append(visit[:])
            return

        # cur부터 n까지 순회 탐색
        for i in range(cur, len(cards)):
            new_visit = visit + [cards[i]]

            # cur이 추가된 시점의 동일 레벨의 재귀 작업
            # 조합이므로 cur이 이미 방문 처리된 new_visit을 할당
            dfs(i + 1, new_visit)

    dfs(0, [])

    return result


# 입력 단계
length, value = map(int, input().split())
cards = list(map(int, input().split()))


# list comprehension 기반 조합 리스트 요소합 반환
combine_list = combine(cards)
sum_list = [sum(sub) for sub in combine_list]


# 순회해서 최대치 탐색
max_count = 0

for num in sum_list:
    if num <= value:
        if max_count <= num:
            max_count = num

print(max_count)