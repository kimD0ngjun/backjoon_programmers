from sortedcontainers import SortedSet

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stones는 중복된 문자들(대소문자 구별)이 포함된 일련의 문자열이다
        # jewels는 보석으로 분류되는 문자를 가리키는(중복될 일이 없는) 구별 기준이다
        
        # stones에서 중복 문자들을 없애며 문자 종류를 저장한다
        # 파이썬의 set은 자바의 HashSet과 유사한 자료구조
        # 이진트리 기반 검색 강화 set인 SortedSet을 사용하면 검색 속도가 향상
        # 자바의 TreeSet
        refined_stones = SortedSet(stones)
        
        # refined_stones와 jewels의 교집합을 계산한다
        # intersection 메소드를 활용한다
        included_jewel = refined_stones.intersection(jewels)
        
        # 하나씩 몇 개가 포함됐는지 count 메소드 활용
        count = 0
        
        for jewel in included_jewel:
            count += stones.count(jewel)
            
        return count