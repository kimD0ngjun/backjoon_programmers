from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 0 배열로 초기화하면서 0 할당 로직 줄이기
        result = [0] * len(temperatures)
        queue = deque()
        
        for i in range(len(temperatures)):
            while queue and temperatures[i] > temperatures[queue[-1]]:
                prev = queue.pop()
                result[prev] = i - prev
                
            queue.append(i)
        
        return result