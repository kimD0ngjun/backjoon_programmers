INF = float("inf")

def bellman_ford(V, edges, sv):
    min_distances = [INF] * (V + 1)
    min_distances[sv] = 0

    # V-1 횟수만큼만 반복, 여기서 한번 더 반복했는데 숫자 변화가 생기면 음의 사이클이 있다고 생각
    for i in range(1, V + 1):
        for start, end, weight in edges:
            if min_distances[start] == INF:
                continue

            next_distance = weight + min_distances[start]
            if next_distance < min_distances[end]:
                min_distances[end] = next_distance

                # 음수 사이클 발견되면 -1 출력 후 프로그램 전체 종료
                # 애시당초 음수 사이클이 있으면 최단 거리 정의가 불가능해짐
                if i == V:
                    print(-1)
                    return

    for i in range(2, N + 1):
        if min_distances[i] == INF:
            print(-1)
        else:
            print(min_distances[i])

edges = []
N, M = map(int, input().split())

for _ in range(M):
    edges.append(list(map(int, input().split())))

bellman_ford(N, edges, 1)

