import heapq

# 파이썬에서의 힙은 최소 힙이 기본 세팅
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
        # nlargest 함수는 내부적으로 최소 힙을 사용
        # 주어진 리스트에서 가장 큰 k개의 요소를 반환
        # 그중 마지막 인덱스에 있는 값이 k번째 최대값
        kth_largest = heapq.nlargest(k, heap)[-1]
        return kth_largest