# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head에서부터 있는 것들 전부 배열에 담기
        check = []
        
        node = head
        
        while node:
            check.append(node.val)
            node = node.next
        
        reverse_check = list(reversed(check)) 
        
        # 역순 노드 생성
        reverse_node = ListNode()  # 더미 노드 생성
        current = reverse_node
        
        for val in reverse_check:
            current.next = ListNode(val)
            current = current.next
        
        return reverse_node.next