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
        
        # 역순 노드 생성
        reverse_node = ListNode() 
        current = reverse_node
        
        for i in range(len(check) - 1, -1, -1):
            current.next = ListNode(check[i])
            current = current.next
        
        return reverse_node.next