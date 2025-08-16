# https://www.acmicpc.net/board/view/145922
import heapq
import sys
from collections import deque


def sys_input():
    return sys.stdin.readline().strip()

routes = {}
input()
# 노드 수, 최대 상한 비용, 간선 수
N, M, K = map(int, sys_input().split())

for _ in range(K):
    # 출발 공항, 도착 공항, 비용, 소요 시간(*)
    s, e, w, t = map(int, sys_input().split())

    if s not in routes:
        routes[s] = [(e, w, t)]
    else:
        routes[s].append((e, w, t))

# 비용 기준 정렬, bfs에서 팝할 때 비용이 더 작은 애들이 먼저 팝핑되면서 간선 탐색 순서 업
for node in routes:
    routes[node].sort(key=lambda x: x[2])

# 1부터 N까지
# def dijkstra(start, end):
#     inf = float("inf")
#     """
#     - 상태 확장
#     전체 탐색 과정에서 해당 노드에 도착했을 때, 비용이 다양한 케이스가 존재함...
#     특정 비용으로 도착했을 때, 그때 최소 거리 갱신 방식으로?
#     [{비용: 최소 시간, 비용: 최소 시간....}, {비용: 최소 시간, 비용: 최소 시간....}, {비용: 최소 시간, 비용: 최소 시간....}...]
#     각 노드별 소요 비용 경우의 수에 따른 각 최소 소요 시간
#
#     수정, 맵 대신 리스트?
#     수정2. priority_queue에 {시간, 노드} 쌍만 넣고 비용은 '최대 비용을 사용한 채 다음 노드에 도달했을 때 소요 시간이 줄어들 때만 pq에 push'하면 시간을 더 줄일 수 있습니다...
#     라는 글을 보았다...
#
#     어떤 노드에 도달할 때, 얼만큼의 비용을 남기고 도달했는지, 그때까지 소요된 시간이 얼만지 모아서 따로따로 기록함
#     현재 힙이 느려지는 건, 같은 노드와 같은 시간에 대해 다른 비용값들이 너무 많아서 그런듯한데, 즉 시간 a * 비용 b 갯수만큼 더 증가
#
#     min_times[node][cost] = 걸린 최소 시간이 항상 갱신되도록
#
#     수정 3, 13퍼 시간초과,,, 그래도 2퍼 시간초과보단 나아졌네..;
#
#     비용에 대한 정보를 현재 내 코드에서 알 수 있는 곳은 3군데
#     routes 변수: 특정 노드를 중심으로 다른 노드까지 가는데 드는 비용 정보
#     힙: 특정 노드까지 특정 시간만큼 소요해서 도달했을 떄, 소요한 비용 정보
#     dp 배열: 특정 노드에서 특정 비용 소모했을 때의 최소 이득 시간 정보
#     """
#     min_times = [[inf] * (M+1) for _ in range(N+1)]
#     min_times[start][0] = 0
#     end_min_time = inf # 또다른 최적화, 도착점 걍 미리미리 계산시켜놓기
#
#     queue = []
#     heapq.heappush(queue, (min_times[start][0], start, 0)) # 최소 시간, 노드, 드는 비용
#
#     while queue:
#         cur_time, cur_node, cur_cost = heapq.heappop(queue)
#
#         if cur_node == end and cur_time < end_min_time:
#             end_min_time = cur_time
#             continue
#
#         # 해당 공항에서 갈 길이 없으면 소비
#         if cur_node not in routes:
#             continue
#
#         # 최적화
#         """
#         같은 비용으로 도착했을 때, 아직 한계시간까지 많이 남은 케이스에 대한 최적화 처리
#         """
#         if min_times[cur_node][cur_cost] < cur_time:
#             continue
#
#         for adj_city, cost, time in routes[cur_node]:
#             updated_time = cur_time + time
#             updated_cost = cur_cost + cost
#
#             # 예산 오버되면 소비
#             if updated_cost > M:
#                 continue
#
#             if updated_time < min_times[adj_city][updated_cost]:
#                 min_times[adj_city][updated_cost] = updated_time
#                 heapq.heappush(queue, (updated_time, adj_city, updated_cost))
#
#                 """
#                 같은 시간을 소요해 도착했을 때, 다양한 비용의 경우 케이스들에 대한 최적화
#
#                 특정 비용에서 더 적은 시간만 써서 도달하는 경우가 확인됐기 때문에, 상식적으로 더 큰 비용을 써서 더 많은 시간을 쓰는 경우는 당연히 손해고
#                 더 큰 비용을 쓰는 건 보통 더 적은 시간만 쓰려고 하기 위함이니 그 마지노선을 현재 분기에서 계산해 얻은
#                 '특정 비용에서 더 적은 시간만 써서 도달하는 경우'를 더 큰 비용의 경우에도 전파시키기 위함
#                 """
#                 for c in range(updated_cost + 1, M + 1):
#                     if min_times[adj_city][c] <= updated_time:
#                         break
#                     min_times[adj_city][c] = updated_time
#
#     # res = min(min_times[end])
#     # if res == inf:
#     #     print("Poor KCM")
#     # else:
#     #     print(res)
#     if end_min_time == inf:
#         print("Poor KCM")
#     else:
#         print(end_min_time)

"""
13% 돌파하기
성과: 32퍼 시간초과
"""
def bfs(start, end):
    inf = float("inf")
    min_times = [[inf] * (M + 1) for _ in range(N + 1)]
    min_times[start][0] = 0
    end_min_time = inf  # 또다른 최적화, 도착점 걍 미리미리 계산시켜놓기

    queue = deque()
    queue.append((min_times[start][0], start, 0)) # 최소 시간, 노드, 드는 비용

    while queue:
        cur_time, cur_node, cur_cost = queue.popleft()

        if cur_node == end and cur_time < end_min_time:
            end_min_time = cur_time
            continue

        if cur_node not in routes:
            continue

        if min_times[cur_node][cur_cost] < cur_time:
            continue

        for adj_city, cost, time in routes[cur_node]:
            updated_time = cur_time + time
            updated_cost = cur_cost + cost

            if updated_cost > M:
                continue

            if updated_time < min_times[adj_city][updated_cost]:
                min_times[adj_city][updated_cost] = updated_time
                queue.append((updated_time, adj_city, updated_cost))

                for c in range(updated_cost + 1, M + 1):
                    if min_times[adj_city][c] <= updated_time:
                        break
                    min_times[adj_city][c] = updated_time

    if end_min_time == inf:
        print("Poor KCM")
    else:
        print(end_min_time)

# dijkstra(1, N)
bfs(1, N)