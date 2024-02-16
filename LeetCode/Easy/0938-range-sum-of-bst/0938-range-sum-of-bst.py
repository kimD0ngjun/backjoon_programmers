# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # exception
        if not root:
            return 0
        
        # BST는 부모를 중심으로 크냐 작냐 이므로
        total_val = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            # 백트랙킹이랑 스택 할당을 한 번에
            if node:
                if low <= node.val <= high:
                    total_val += node.val
                    
                if node.val > low:
                    stack.append(node.left)
                    
                if node.val < high:
                    stack.append(node.right)
        
        return total_val