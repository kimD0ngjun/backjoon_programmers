# Both rows have the same number of soldiers and i < j.
# 나중에 힙에 추가되어도 스왑이 일어나지 않고 밑으로 배치될 테니 무관
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:       
        # list comprehension으로 리스트 총합으로 매핑
        sum_list = [sum(el) for el in mat]
        
        # 해당 값과 인덱스(추적용)를 리스트화(enumerate)해서 최소 힙에 넣기
        heap = [(el, index) for index, el in enumerate(sum_list)]
        heapq.heapify(heap)
        
        # k번째 최소합 인덱스까지 뽑아내기
        result = []
        for i in range(k):
            value, index = heapq.heappop(heap)
            result.append(index)
        
        return result
        
        