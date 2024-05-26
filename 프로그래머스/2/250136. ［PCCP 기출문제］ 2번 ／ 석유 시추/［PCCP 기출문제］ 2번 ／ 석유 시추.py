from collections import deque, defaultdict

def solution(land):
    """
    땅 : 0
    석유 : 1
    탐사 완료 : 2, 3, 4 ....(이걸 딕셔너리로 저장해서 마주하는 석유 체임버는 미리 조회 계산?)
    """

    search_range = len(land[0])
    depth = len(land)
    max_value = 0
    search_memory = defaultdict(int)
    memory = 2
    answer = []

    dx = [1, -1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # 순차적으로 탐색 시작
    for search_point in range(search_range):

        values = {}

        # 각 깊이에 따른 탐색 시작
        for depth_point in range(depth):

            # 석유 발견?
            if land[depth_point][search_point] == 1:

                value = 1 # 석유 양
                land[depth_point][search_point] = memory # 탐색 완료 표시
                queue = deque()
                # (시작지점 x좌표, y좌표)
                queue.append((search_point, depth_point))

                # 어차피 뭉쳐진 하나의 석유 체임버만 탐색할뿐
                while queue:
                    search_value, depth_value = queue.popleft()

                    for i in range(4):
                        next_search_value = search_value + dx[i]
                        next_depth_value = depth_value + dy[i]

                        # 탐색 범위 벗어나면 컨티뉴
                        if not (0 <= next_search_value < len(land[0]) and 0 <= next_depth_value < len(land)):
                            continue

                        # 땅이거나 탐색했으면 컨티뉴
                        if land[next_depth_value][next_search_value] == 0 or land[next_depth_value][next_search_value] == memory:
                            continue

                        # 석유 발견
                        if land[next_depth_value][next_search_value] == 1:
                            value += 1
                            land[next_depth_value][next_search_value] = memory
                            queue.append((next_search_value, next_depth_value))

                search_memory[memory] = value
                values[memory] = value
                memory += 1

            elif land[depth_point][search_point] in search_memory and land[depth_point][search_point] not in values:
                values[land[depth_point][search_point]] = search_memory[land[depth_point][search_point]]

        answer.append(sum(values.values()))

    # print(answer)

    return max(answer)