from queue import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # visit = []
        # visit = {1: False, 2: False, 3: False}
        # visit = set()
        
        queue = deque()
        queue.append([nums, []])
        result = []
        
        # 예외 처리
        if len(nums) is 1:
            return [[], nums]
        
        # 작업 처리        
        while queue:
            remaining, path = queue.popleft()
            result.append(path)

            
            for i in range(len(remaining)):
                new_remaining = remaining[i+1:]
                new_path = path + [remaining[i]]
                
                queue.append([new_remaining, new_path])
            
            
        return result
                    
                