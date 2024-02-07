# Definition for singly-linked list.
# 그냥 양방향 연결 리스트를 구현해서 투포인터처럼 풀면 되지 않나?
# 아니네 넣는 순서의 역순으로 넣으면 되겠네
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # head에 있는 애들 전부 배열에 담기
        check = []
        
        node = head
        
        while node:
            check.append(node.val)
            node = node.next
        
        if len(check) <= 1:
            return True
        
        while len(check) > 1:
            if check.pop() != check.pop(0):
                return False
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        