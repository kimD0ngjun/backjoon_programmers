# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 비어있거나 노드 한 개만 있는 경우
        if head == None or head.next == None:
            return head
        
        # 역방향 포인터 지정
        # 처음 노드부터 시작
        # (해당 노드의 next는 None이 되고, 자기 자신은 다음 단계의 포인터가 되어야 한다)
        current = head
        reverse = None

        while current != None: # 다음 단계 노드가 None이면 끝까지 훑은 거니까
            # 다음 단계를 위한 임시 저장
            next_phase = current.next
            
            # 현재 노드의 포인터(다음 방향)을 역방향으로 뒤집음
            current.next = reverse
            
            # 역순의 방향은 현재 처리된 노드가 되도록 할당
            reverse = current
            
            # 다음 단계로 넘어감
            current = next_phase
            
        return reverse
        
### 배열로 변환해서 풀이 ###

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # head에서부터 있는 것들 전부 배열에 담기
#         check = []
        
#         node = head
        
#         while node:
#             check.append(node.val)
#             node = node.next
        
#         # 역순 노드 생성
#         reverse_node = ListNode() 
#         current = reverse_node
        
#         for i in range(len(check) - 1, -1, -1):
#             current.next = ListNode(check[i])
#             current = current.next
        
#         # 머리 노드(reverse_node)와 그 머리 노드의 포인터(reverse_node.next)만 알면
#         # 전체 연결 리스트를 알 수 있으므로 reverse_node.next를 리턴
#         return reverse_node.next