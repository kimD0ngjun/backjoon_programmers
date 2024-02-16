import sys
from collections import deque

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 재귀 탐색 함수
def dfs(node_list, idx):
    # 현재 시점 방문 표기
    node_list[idx] = None
    
    # 노드 리스트 순회해서 현재 노드를 부모로 갖는 값의 인덱스 탐색
    for i in range(len(node_list)):
        if idx == node_list[i]:
            dfs(node_list, i)

# 카운팅 함수
def counting_node(node_list):
    count = 0
    
    # 노드 리스트 순회
    for i in range(len(node_list)):
        # 현재 노드가 None이 아니라면(삭제되지 않았다면)
        if node_list[i] != None:
            # 해당 노드가 부모를 갖지 않는다면(연결된 다른 노드가 없다면)
            if i not in node_list:
                # 카운트 증가
                count += 1
            
    return count

# 입력 처리
node_count = int(sys_input())
node_list = list(map(int, sys_input().split()))
delete_node = int(sys_input())

# 출력 처리
dfs(node_list, delete_node)
count = counting_node(node_list)
print(count)
