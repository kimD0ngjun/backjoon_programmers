# 아 문제 설명 진짜 드릅게 가독성 떨어지네
# 1 : 루트 노드
# 단위 입력에서 두 개의 입력 : 노드와 노드 간의 간선 설정(누가 부모 노드인진 찾아가는 게 문제)
# 출력 : 노드의 부모

import sys
from collections import deque

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 트리 생성 함수
def trace_parent(edges, tree):
    queue = deque([1])
    # 부모 노드 추적(1은 그냥 0 설정) 초기화
    parent_node = [0] * (edges + 1)

    while queue:
        current = queue.popleft()
        
        for i in tree[current]:
            # 1은 루트 노드
            if parent_node[i] == 0 and i != 1:
                parent_node[i] = current
                queue.append(i)
                
    return parent_node

# 입력 처리
edges = int(sys_input())
tree = {}

# 트리 세팅
for i in range(1, edges + 1):
    tree[i] = []

# 간선 정보 추가
for _ in range(edges - 1):
    node_one, node_another = map(int, sys_input().split())
    
    tree[node_one].append(node_another)
    tree[node_another].append(node_one)

parent_node = trace_parent(edges, tree)

for i in range(2, edges + 1):
    print(parent_node[i])
