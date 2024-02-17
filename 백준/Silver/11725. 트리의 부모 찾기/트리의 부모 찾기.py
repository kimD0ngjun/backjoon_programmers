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
    # 루트 노드(1)를 넣음으로써 초기화한다
    queue = deque([1])
    # 부모 노드 추적(1은 그냥 0 설정) 리스트 초기화
    # 인덱스(= 자식 노드 값), 인덱스에 해당하는 값(= 부모 노드 값)
    parent_node = [0] * (edges + 1)

    # 큐가 비워질 때까지(노드의 부모를 전부 추적할 때까지)
    while queue:
        # 예를 들어 1이 뽑혔다
        current = queue.popleft()
        
        # 1의 자식인 6과 4를 순회(1이 이미 부모 확정인 이상 6과 4는 자식이 되어야 한다)
        # 이 시점에서 tree[current]에 속한 리스트의 요소들은 자식 확정인 셈
        for i in tree[current]:
            # 추적이 안 된 자식들(얘네 역시 누군가의 부모가 될 수 있으니) 할당
            # 1은 루트 노드니까 배제
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
# 사실 트리의 특성상 단방향이어야 하지만 현재는 양방향이어도 무방
# 어차피 연결된 것들 중 한 노드가 부모가 되면 다른 노드는 자연히 자식이 될 터이니
for _ in range(edges - 1):
    node_one, node_another = map(int, sys_input().split())
    
    tree[node_one].append(node_another)
    tree[node_another].append(node_one)

parent_node = trace_parent(edges, tree)

for i in range(2, edges + 1):
    print(parent_node[i])
