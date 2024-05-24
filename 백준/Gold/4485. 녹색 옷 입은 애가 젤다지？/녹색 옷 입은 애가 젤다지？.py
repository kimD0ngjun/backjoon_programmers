import heapq
from collections import defaultdict

# 그래프 초기화
graph = defaultdict(dict)

# 다익스트라 함수 + bfs
def dijkstra(maps, length):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    inf = float('inf')
    # 지도의 각 정점별 최단 가중치 초기화
    min_distances = [[inf] * length for _ in range(length)]

    queue = []
    # 큐, 가중치, x좌표, y좌표
    heapq.heappush(queue, (maps[0][0], 0, 0))
    min_distances[0][0] = 0

    while queue:
        cur_weight, x, y = heapq.heappop(queue)

        # 도착 제어
        if x == length - 1 and y == length - 1:
            return min_distances[x][y]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < length and 0 <= next_y < length:
                updated_weight = cur_weight + maps[next_x][next_y]

                if updated_weight < min_distances[next_x][next_y]:
                    min_distances[next_x][next_y] = updated_weight
                    heapq.heappush(queue, (updated_weight, next_x, next_y))


## 입력 처리
count = 0
results = []

while True:
    length = int(input())

    if length == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(length)]

    result = dijkstra(maps, length)
    results.append(result)
    count += 1

for i in range(0, count):
    print(f'Problem {i + 1}: {results[i]}')