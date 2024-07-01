"""
https://www.acmicpc.net/problem/1967
"""
from collections import defaultdict

# 입력 받기
n = int(input())

# 부모 : {자식: 가중치, 자식: 가중치...}
tree = defaultdict(list)
distance = {}

"""
상위 노드, 하위 노드, 가중

항상 시작점은 리프 노드
역방향 dfs?

"""

for _ in range(n - 1):
    a, child, weight = map(int, input().split())
    tree[a].append((child, weight))
    tree[child].append((a, weight))


def dfs(start, parent):
    stack = [(start, parent)]

    while stack:
        cur_node, node_parent = stack.pop()

        # 현재 팝된 노드들의 자식 노드들 전부 뽑아내기
        for child_node, weight_value in tree[cur_node]:
            if child_node == node_parent:  # 부모 노드로 돌아가는 경우를 방지
                continue

            # 현재 노드 및 이어진 간선 가중치 더함으로써 자식 노드까지의 거리 업데이트
            distance[child_node] = distance[cur_node] + weight_value
            stack.append((child_node, cur_node))


# 루트 노드에서 모든 노드까지 거리 dfs로 계산
# 루트 노드의 번호는 항상 1(당연히 거리는 0), 부모 노드가 없을 테니 -1 초기화
distance[1] = 0
dfs(1, -1)

# 가장 먼 (리프) 노드 찾기

# 초기화 후 순회하면서 탐색
far_node = 1
max_distance = 0

for node in distance:
    if distance[node] > max_distance:
        far_node = node
        max_distance = distance[node]

"""
다시 재활용하면 됐네;
"""

# 거리 재활용
for key in distance.keys():
    distance[key] = 0

# 먼 노드 기점으로 계산 다시 시작
distance[far_node] = 0
dfs(far_node, -1)

# 트리의 지름 계산
diameter = max(distance.values())
print(diameter)
