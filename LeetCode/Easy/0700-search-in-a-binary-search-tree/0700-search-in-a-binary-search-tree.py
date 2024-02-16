# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # exception
        if not root:
            return None
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                # 백트랙킹
                # 그냥 노드의 값과 일치하면 바로 리턴하면 되잖...??
                if node.val == val:
                    return node
                
                if node.left:
                    stack.append(node.left)
                    
                if node.right:
                    stack.append(node.right)
                    
        
            