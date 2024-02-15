# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 텅 빈 트리(초기값) 선언
        self.diameter = 0
        
        # 계산이 될 경우, 해당 값으로 diameter 업데이트
        self.dfs(root)
        
        return self.diameter

    # dfs 재귀
    def dfs(self, root: TreeNode) -> int:
        # 탈출조건
        if not root:
            return 0
        
        # '현재 단계'에서의 좌우 자식노드
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        
        # 깊이 값 동적 업데이트
        self.diameter = max(self.diameter, left_depth + right_depth)
        
        # '현재 단계'에서 깊이 1씩 증가
        return max(left_depth, right_depth) + 1
        
        
    
        