import heapq

# nlargest는 내부 정렬 과정이 포함된다
# nlargest를 쓰지 말고 풀어보자
class Solution:    
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        # 최대 힙으로 세팅하기 위한 요소 음수배
        for num in nums:
            heapq.heappush(heap, -num)
        
        # 최대값이 현 힙 내에서는 가장 작은 값
        minus_max = heapq.heappop(heap)
        max = - minus_max
        
        minus_second_max = heapq.heappop(heap)
        second_max = - minus_second_max
        
        return (max - 1) * (second_max - 1)