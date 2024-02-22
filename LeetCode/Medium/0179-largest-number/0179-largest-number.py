class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 스트링화한 숫자와 늘인 숫자 이중 리스트
        compare = []

        for num in nums:
            str_num = str(num) # 숫자를 문자열로 변환

            extended_str = str_num * 10  # 반복
            compare.append([str_num, extended_str])

        # 두 숫자를 비교할 때는, 두 숫자를 연결한 경우의 크기를 비교하여 정렬
        sorted_list = sorted(compare, key=lambda x: x[1], reverse=True)
        combined_string = ''.join([item[0] for item in sorted_list])
        
        # exception
        if combined_string[0] == '0':
            return "0"
        
        return combined_string
    
    """1차 잘못된 시도"""
    # 자릿수를 같게 만들어서 비교하면 되지 않으려나?
    # 예를 들어서 9와 34와 5를 비교할 때는
    # 9000, 3400, 5000 이런 식으로 자릿수를 통일시켜서 비교하면 될듯?
    # 뒤에 0이 9개 붙어야겠네

    # 반례 : 111311, 1113
    
    """2차 시도"""
    # 0을 붙이는 것이 아닌 숫자 자체를 반복해서 두 개를 직접 이어붙인 후 그 결과를 비교
    # 그렇게 하면 반복 숫자에서 앞선 것이 무조건 결합했을 때 크기가 앞서게 되므로
    # 사전식 순서로