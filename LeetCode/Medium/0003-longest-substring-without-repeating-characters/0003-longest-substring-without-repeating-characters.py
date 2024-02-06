class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 투포인터 알고리즘이랑 set 접목시키기
        length = len(s)
        
        # 탐색한 부분 문자열들 중 최대 길이(업데이트용)
        max_len = 0
        
        # 인덱스 0에서 투포인터 시작
        left = 0
        right = 0
        
        # 중복 필터용 set 집합
        seen = set()

        # right 포인터가 멈추는 이유(else 구문)은
        # 반복되는 문자를 찾아서 문제의 substring 조건을 만족하지 못하기 때문
        # 이에 left 포인터를 옮겨서 새로운 문자열 탐색을 시작해야 된다
        while right < length:
            if s[right] not in seen:
                # 일반적인 right 탐색 과정
                seen.add(s[right])
                right += 1
                
                # 최대 길이 업데이트
                max_len = max(max_len, right - left)
            else:
                # 이미 set 집합에 있으면 해당하는 문자를 집합에서 제외한다
                seen.remove(s[left])
                
                # 그 시점에서 중복된 substring이 되므로
                # left 포인터를 한 칸 앞으로 당겨서 새로운 문자열 탐색을 시작한다
                left += 1
                
                # 어차피 left 포인터가 옮겨지면서 최대 길이보다 짧으므로
                # 굳이 업데이트 로직 포함 불필요

        return max_len