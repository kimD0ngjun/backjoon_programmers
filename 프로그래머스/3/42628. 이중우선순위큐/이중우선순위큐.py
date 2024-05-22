import sys
# import heapq

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

# 이진탐색트리
class BinarySearchTree:
    def __init__(self):
        self.root = None

    """
    루트발 삽입
    """
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)

    # 부모 자식 단위에서 자식으로 넘겨주기
    def insert_node(self, node: Node, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_node(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_node(node.right, value)

    """
    루트발 삭제
    """
    def delete(self, value: int) -> None:
        self.root = self.delete_node(self.root, value)

    # 삭제 재귀 단위
    def delete_node(self, node: Node, value: int):
        if node is None:
            return

        # 만약 삭제 노드가 현 노드보다 작으면
        if value < node.value:
            # 자연히 왼쪽으로 흘러가기
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            # 그 반대라면 오른쪽으로 흘러가기
            node.right = self.delete_node(node.right, value)

        # 만약 삭제할 노드를 발견했을 경우
        else:
            # 리프 노드(형제 없는 노드)면 바로 반환
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 두 자식 다 존재하면...
            # 삭제 대상 노드와 오른쪽 서브트리의 가장 왼쪽 노드(가장 작은 노드)와 위치 바꾸기
            # 위치 바뀐 삭제 대상 노드 거슬러 타고 올라가며 구조 조정
            temp_val = self.min_value_node(node.right)
            node.value = temp_val.value
            node.right = self.delete_node(node.right, temp_val.value)

        # 변경된 루트노드 반환
        return node


    """
    루트발 재귀호출 기반 최소값 탐색
    """
    def find_min(self):
        if self.root is None:
            return None
        return self.min_value_node(self.root).value

    # 서브트리 기반 노드 탐색(최소)
    def min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    """
    루트발 재귀호출 기반 최대값 탐색
    """
    def find_max(self):
        if self.root is None:
            return None
        return self.max_value_node(self.root).value

    # 서브트리 기반 노드 탐색(최대)
    def max_value_node(self, node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current

    def search(self, value: int) -> bool:
        return self.search_node(self.root, value)

    def search_node(self, node: Node, value: int) -> bool:
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.search_node(node.left, value)
        else:
            return self.search_node(node.right, value)

        

def solution(operations):
    """
    이진탐색트리 기반 풀이
    """
    
    bst = BinarySearchTree()
    
    for i in range(len(operations)):
        value = operations[i]

        if value[:1] == "I":
            int_value = int(value[2:])
            bst.insert(int_value)

        elif value[:1] == "D":
            if value[2:] == "1":
                bst.delete(bst.find_max())
            elif value[2:] == "-1":
                bst.delete(bst.find_min())

    if bst.find_max() is None:
        return [0, 0]
    else:
        return [bst.find_max(), bst.find_min()]
    
    
    
    
    """
    힙 기반 풀이
    """
#     max_heap = []
#     min_heap = []
#     is_deleted = [False] * len(operations)
    
#     for i in range(len(operations)):
#         value = operations[i]
        
#         # 삽입
#         if value[:1] == "I":
#             int_value = int(value[2:])
#             heapq.heappush(min_heap, (int_value, i))
#             heapq.heappush(max_heap, (-int_value, i))
        
#         # 삭제
#         elif value[:1] == "D":
#             if value[2:] == "1":
#                 if len(max_heap) > 0:
#                     is_deleted[heapq.heappop(max_heap)[1]] = True
#             elif value[2:] == "-1":
#                 if len(min_heap) > 0:
#                     is_deleted[heapq.heappop(min_heap)[1]] = True

#         # 삭제 동기화
#         while len(max_heap) > 0 and is_deleted[max_heap[0][1]] == True:
#             heapq.heappop(max_heap)

#         while len(min_heap) > 0 and is_deleted[min_heap[0][1]] == True:
#             heapq.heappop(min_heap)
    
#     if len(min_heap) == 0:
#         return [0, 0]
#     else:
#         return [-max_heap[0][0], min_heap[0][0]]
