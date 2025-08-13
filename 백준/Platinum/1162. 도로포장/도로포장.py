import heapq
import sys
from collections import defaultdict

def sys_input():
    return sys.stdin.readline().strip()

cities = {}
N, M, K = map(int, sys_input().split())

for _ in range(M):
    s, e, w = map(int, sys_input().split())

    if s not in cities:
        cities[s] = [(e, w)]
    else:
        cities[s].append((e, w))

    if e not in cities:
        cities[e] = [(s, w)]
    else:
        cities[e].append((s, w))

def dijkstra(start, end):
    inf = float("inf")
    min_costs = [[inf] * (K + 1) for _ in range(N + 1)] # 포장 카운트에 따른 해당 노드까지의 최소 거리
    min_costs[start][0] = 0

    queue = []
    heapq.heappush(queue, (min_costs[start][0], start, 0)) # 최소 거리, 노드, 포장 카운트

    while queue:
        cur_cost, cur_dir_city, count = heapq.heappop(queue)

        if min_costs[cur_dir_city][count] < cur_cost:
            continue

        for adj_city, cost in cities[cur_dir_city]:
            updated_cost = cur_cost + cost

            # 포장하지 않고 이동
            if updated_cost < min_costs[adj_city][count]:
                min_costs[adj_city][count] = updated_cost
                heapq.heappush(queue, (updated_cost, adj_city, count))

            # 포장하고 이동
            # 아.. 업데이트한 값이 아니라 그냥 현재값으로 비교해야되지..? 어차피 cost가 0인걸 가정하니까...
            if count < K and cur_cost < min_costs[adj_city][count + 1]:
                min_costs[adj_city][count + 1] = cur_cost # 추가한 cost가 0이므로
                heapq.heappush(queue, (cur_cost, adj_city, count + 1))

    return min(min_costs[end])

print(dijkstra(1, N))