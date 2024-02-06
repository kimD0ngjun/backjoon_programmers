class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []        
        
        # 조건 부합 카운팅 변수와 최대 길이
        length = len(nums)
        count = 0
        
        # HashMap 개념을 써서 각 요소 별 등장 횟수를 세리는 게 옳을 것 같음
        # 투 포인터는 인덱스 개념이 포함된 문제에서 유용한데
        # 현재 문제는 인덱스와 무관하게 등장 횟수만을 세리는 것에 불과함
        
        # 자바의 HashMap과 유사한 구조인 파이썬의 defaultdict
        counts = defaultdict(int)
        
        # 카운팅
        for num in nums:
            counts[num] += 1
            
        # 내림차순으로 가장 많은 횟수를 가진 키-쌍들로 정렬시킴
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # k 이상의 횟수에 상응하는 키들만 모아서 리스트화 
        result = [item[0] for item in sorted_counts[:k]]
        
        return result