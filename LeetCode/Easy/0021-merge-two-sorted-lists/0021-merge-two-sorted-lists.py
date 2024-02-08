# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 일반 배열 리스트에 비해 연결 리스트는 삽입과 삭제가 빠르다
        # 포인터 취지 살려서 작성해보기
        one_node = list1
        other_node = list2
        
        # 예외 처리
        if one_node == None:
            return other_node
        elif other_node == None:
            return one_node
        elif one_node == None and other_node == None:
            return None
        
        # 병합 리스트 선언
        new_head = None
        
        if one_node.val > other_node.val:
            new_head = other_node
            other_node = other_node.next
        else:
            new_head = one_node
            one_node = one_node.next
        
        # 반복 작업 및 현재 노드 추적용 sorted_current
        sorted_current = new_head
        
        while one_node != None and other_node != None:
            # 노드의 값과 다른 노드의 값을 비교한다
            if one_node.val > other_node.val:
                sorted_current.next = other_node
                other_node = other_node.next
                
            else:
                sorted_current.next = one_node
                one_node = one_node.next
    
            sorted_current = sorted_current.next
        
        # 먼저 작업이 끝난 리스트일 경우(즉, 두 리스트의 길이가 다를 경우)
        if one_node == None:
            sorted_current.next = other_node
        elif other_node == None:
            sorted_current.next = one_node
            
        return new_head
        