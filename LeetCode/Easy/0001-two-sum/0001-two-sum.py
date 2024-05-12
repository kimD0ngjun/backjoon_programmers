class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 인덱스 튜플 정보 포함
        tuple_list = list(map(lambda x: (x[1], x[0]), enumerate(nums)))
        
        # 조합 걸러내기
        for i in range(len(tuple_list)):
            for j in range(i + 1, len(tuple_list)):
                if tuple_list[i][0] + tuple_list[j][0] == target:
                    return [tuple_list[i][1], tuple_list[j][1]]