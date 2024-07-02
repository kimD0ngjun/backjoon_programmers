"""
https://www.acmicpc.net/problem/1167
"""
from collections import defaultdict

# 입력 받기
V = int(input())

# 부모 : {자식: 가중치, 자식: 가중치...}
tree = defaultdict(list)
distance = {}

"""
양방향 그래프만 세팅해준 다음에,
리프 노드의 특징 살리기

내가 생각하는 리프 노드의 특징 : 인접 간선이 1개다
지름은 리프 노드에서 리프 노드까지의 거리라서 그걸 구하면 될듯
"""

root = 0

for _ in range(V):
    vertex_info = list(map(int, input().split()))
    vertex_info.pop() # -1 뽑아내기
    vertex = vertex_info[0] # 정점

    # 임의의 루트 할당
    if len(vertex_info) > 3:
        root = vertex

    for i in range(1, len(vertex_info), 2):
        neighbor = vertex_info[i]
        weight = vertex_info[i+1]

        tree[vertex].append((neighbor, weight))
        # tree[neighbor].append((vertex, weight)) # 어차피 중복 정보가 입력값에 다 담겨있음
# 
# print(tree)
# print(root)

"""
리프 노드가 아닌 노드는 루트 노드로 설정하지 않기
사실 리프 노드도 루트 노드가 될 순 있지만 보편적인 트리의 형태와 다를 뿐더러
지름의 연산 조건이 리프 노드이므로 조건의 중복 배제를 위해 일단은 리프 노드가 아닌 노드를 루트 노드로 가정
"""

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
distance[root] = 0
dfs(root, -1)

# 가장 먼 (리프) 노드 찾기

# 초기화 후 순회하면서 탐색
far_vertex = 1
max_distance = 0

for node in distance:
    if distance[node] > max_distance:
        far_vertex = node
        max_distance = distance[node]

# 거리 재활용
for key in distance.keys():
    distance[key] = 0

# 먼 노드 기점으로 계산 다시 시작
distance[far_vertex] = 0
dfs(far_vertex, -1)

# 트리의 지름 계산
diameter = max(distance.values())
print(diameter)
