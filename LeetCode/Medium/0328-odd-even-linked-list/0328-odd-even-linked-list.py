# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        # 홀수 번째, 짝수 번쨰...
        # 시작 지점 저장하기
        odd_head = head
        odd = odd_head
        
        even_head = head.next
        even = even_head
        
        # 짝수 번째 시작 기억해서 홀수 번째 맨 끝에서 이어붙이기
        # 짝수 번쨰가 언제나 꼬리가 될 테니 even을 기준으로
        while even != None and even.next != None:
            # even의 다음 값이 odd의 next로 덧붙이기
            odd.next = even.next
            # odd 업데이트
            odd = odd.next
            
            # even도 마찬가지
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return odd_head
            