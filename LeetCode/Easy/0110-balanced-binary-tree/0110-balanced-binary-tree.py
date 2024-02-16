# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # 반복문으로 작성하려니까 머리 뽀샤지겠다
        def get_height(node: Optional[TreeNode]) -> int:
            # 재귀 탈출조건
            if not node:
                return 0
            
            # 재귀의 역순으로 올라가면서 최대 높이 산출
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # 현재 시점의 높이 + 1(맨 밑바닥에서 실행될 예정)
            return max(left_height, right_height) + 1
        
        # 루트의 왼쪽 노드와 오른쪽 노드에게 각각 재귀함수 적용
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        # 왼쪽, 오른쪽 높이 차이가 1 이하
        if abs(left_height - right_height) <= 1:
            # 현재의 왼쪽 서브트리도 균형 트리
            # 현재의 오른쪽 서브트리도 균형 트리
            # 즉, 모든 서브트리 역시 균형 트리여야 한다
            # 이건 참조한 부분... 파이썬 클래스 문법에 대해 더 숙지해야 함..ㅠ
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        return False
        