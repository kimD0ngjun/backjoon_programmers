import heapq
import sys
from collections import defaultdict

def sys_input():
    return sys.stdin.readline().strip()

N = int(sys_input())
M = int(sys_input())

city = [[] for _ in range(N + 1)]

for _ in range(M):
    depart, arrive, cost = map(int, sys_input().split())
    city[depart].append((arrive, cost))

departure, arrival = map(int, sys_input().split())

def dijkstra(start, end):
    inf = 100_000 * M
    min_costs = [inf] * (N + 1)
    min_costs[start] = 0

    queue = []
    heapq.heappush(queue, (min_costs[start], start))

    while queue:
        cur_cost, cur_dir_city = heapq.heappop(queue)

        if min_costs[cur_dir_city] < cur_cost:
            continue

        for adj_city, cost in city[cur_dir_city]:
            updated_cost = cur_cost + cost

            if updated_cost < min_costs[adj_city]:
                min_costs[adj_city] = updated_cost
                heapq.heappush(queue, (updated_cost, adj_city))

    return min_costs[end]

print(dijkstra(departure, arrival))