# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, diameter: List[int]) -> int:
            # 탈출 조건
            if not root:
                return 0
        
            # 좌우로 나눠서 재귀(각각의 높이 산정)
            left_depth = dfs(root.left, diameter)
            right_depth = dfs(root.right, diameter)
        
            # 현재 시점의 직경 반환
            # 지속적으로 직경 업데이트 하면서 최종적으로 루트 노드 직경 업데이트
            diameter[0] = max(diameter[0], left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        # 지름 리스트 초기화
        diameter = [0]
        dfs(root, diameter)
        
        return diameter[0]
    
    # diameter를 리스트로 사용한 이유는 Python의 한계 때문
    # Python에서는 함수 내부에서 외부의 변수를 수정하기 위해서는 그 변수가 mutable(가변) 타입
    # 리스트는 가변(mutable) 타입이기 때문에 리스트를 사용하여 diameter를 함수 내에서 수정 가능
    # 단순 변수로 쓰려면 nonlocal 키워드를 써야 함

        