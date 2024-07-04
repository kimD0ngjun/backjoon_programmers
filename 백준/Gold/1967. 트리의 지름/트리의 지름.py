from collections import defaultdict, deque

# 입력 받기
n = int(input())

# 노드 : {이웃: 가중치, 이웃: 가중치...}
tree = defaultdict(list)

for _ in range(n - 1):
    node, neighbor, weight = map(int, input().split())
    tree[node].append((neighbor, weight))
    tree[neighbor].append((node, weight))


# start 노드에서 가장 거리가 먼 노드 구하기
def bfs(start):
    # 인덱스 == 노드 번호, 인덱스의 값 == 해당 노드까지의 거리
    # 방문하지 않았다는 표시로써 -1 초기화
    distance = [-1] * (n + 1)
    queue = deque([(start, 0)])
    distance[start] = 0

    while queue:
        cur_node, cur_distance = queue.popleft()

        for neighbor, weight in tree[cur_node]:

            if distance[neighbor] == -1:
                distance[neighbor] = cur_distance + weight
                queue.append((neighbor, cur_distance + weight))

    max_distance = max(distance)

    return distance.index(max_distance), max(distance), distance


# 트리의 지름을 구성하는 노드 A, B 구하기
A, A_max_distance, distances_1 = bfs(1)
B, tree_diameter, distances_A = bfs(A)

print(tree_diameter)