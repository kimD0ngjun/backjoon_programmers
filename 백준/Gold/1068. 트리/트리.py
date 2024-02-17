import sys
from collections import deque


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# 재귀 탐색 함수
def dfs(parent_node_list, delete_node):
    # 삭제 노드의 부모 노드를 None (단절)처리시킨다
    # delete node = 부모 노드 리스트의 인덱스 = 부모 노드 리스트 해당 인덱스(삭제 노드) 요소가 부모
    parent_node_list[delete_node] = None

    # 노드 리스트 순회해서 현재 노드를 부모로 갖는 값의 인덱스 탐색
    for i in range(len(parent_node_list)):
        # 삭제하려는 노드를 부모 노드로 갖는 인덱스(노드)가 있다면 재귀로 추가 삭제 처리
        if delete_node == parent_node_list[i]:
            dfs(parent_node_list, i)


# 카운팅 함수
def counting_node(parent_node_list):
    count = 0

    # 노드 리스트 순회
    for i in range(len(parent_node_list)):
        # 현재 인덱스(노드)의 부모노드가 None이 아니라면
        # 즉, 끊어지지 않으면서 여전히 트리에 매달려 있다(리프 노드 후보)
        if parent_node_list[i] != None:
            # 해당 인덱스(노드)가 부모 노드 리스트에 있다는 것은, 
            # 자신이 갖고 있는 자식(그 해당 노드(인덱스)를 요소로 갖는 하위 개념의 인덱스(노드)이 있다는 뜻
            # 즉, 리프 노드가 아니니까 그 조건은 걸러줘야 한다
            if i not in parent_node_list:
                # 카운트 증가
                count += 1

    return count


# 입력 처리
node_count = int(sys_input())
parent_node_list = list(map(int, sys_input().split()))
delete_node = int(sys_input())

# 출력 처리
dfs(parent_node_list, delete_node)
count = counting_node(parent_node_list)
print(count)
