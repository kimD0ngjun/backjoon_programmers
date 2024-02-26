class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # 메모이제이션
        
        return self.recursion(n, memo)
    
    # 두 칸 올라가고 한 칸 올라가고... 결국 k칸 올라갔을 때 가짓수는 늘 두 가지(1칸 / 2칸)
    # 반대로 내려가는 거로 생각해보자
    def recursion(self, n, memo):
        # n이 0이란 말은 딱 맞춰서 내려왔단 의미니까 경우의 수 추가
        if n == 0:
            return 1
        # n이 0보다 작다면 결국 들어맞지 못하단 의미니까 경우의 수 x
        elif n < 0:
            return 0
        
        # 메모이제이션 : 이미 저장된 이전 계산값이 있으면 굳이 재귀로 파고들지 않고 바로 리턴
        if n in memo:
            return memo[n]
        
        # 모든 케이스든 무조건 한 칸, 혹은 두 칸 내려가는 경우로 갈리니까
        memo[n] = self.recursion(n-1, memo) + self.recursion(n-2, memo)
        
        return memo[n]
        
        
#     # dfs로 푸니까 시간초과가 뜨는군... 정답은 맞는디
#     def dfs(self, n):
#         stack = [(0, 0)]  # start, sum_amount
#         neighbors = [1, 2]
#         count = 0
    
#         while stack:
#             current, sum_amount = stack.pop()
#             sum_amount += current 
        
#             if sum_amount == n: 
#                 count += 1
        
#             if sum_amount > n: 
#                 continue  # 팝만 된 상태로 스택이 한 칸 비워짐
        
#             for neighbor in neighbors:
#                 stack.append((neighbor, sum_amount)) 
    
#         return count